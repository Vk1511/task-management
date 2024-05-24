from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

# To get AUTH_USER_MODEL from settings.py file
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    # User Password will not be sent as response
    password = serializers.CharField(write_only=True)

    class Meta(object):
        model = User
        # fields required to be serialized for Registration
        fields = [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "password",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def validate(self, attrs):
        password = attrs.get("password")
        user = User(**attrs)
        validate_password(password=password, user=user)
        return super().validate(attrs)


class UserProfileSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):

        data = super().to_internal_value(data)
        if self.instance:
            for field in self.Meta.create_only_fields:
                if field in data:
                    data.pop(field)
        return data

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "date_of_birth",
            "is_superuser",
        )

        read_only_fields = ("is_superuser",)

        create_only_fields = ("is_developer",)

        # "email" field inside AccountableUser Model is required field
        # But here we need "email" as optional request parameter
        # To do that we need following change
        extra_kwargs = {"email": {"required": False}}

    def update(self, instance, validated_data):
        instance.email = validated_data["email"]
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.date_of_birth = validated_data["date_of_birth"]
        instance.save()


class UserPasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "new_password",
            "old_password",
        )

    def validate(self, attrs):
        user = self.context["request"].user
        old_password = attrs.get("old_password")
        new_password = attrs.get("new_password")
        valid_old_password = user.check_password(old_password)

        if not valid_old_password:
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"}
            )

        validate_password(new_password, user=user)
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance
