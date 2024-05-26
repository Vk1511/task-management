from rest_framework import serializers
from .models import UserTask, TaskComments
from django.contrib.auth import get_user_model
from datetime import datetime

# To get AUTH_USER_MODEL from settings.py file
User = get_user_model()


class UserTaskSerializer(serializers.ModelSerializer):
    # TODO: need to add created by only for super user while fetching data
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    assigned_to = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="email", required=False
    )

    class Meta:
        model = UserTask
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "status",
            "due_date",
            "is_public",
            "created_by",
            "created_at",
            "updated_at",
            "assigned_to",
            "assigned_at",
        ]
        read_only_fields = ["created_at", "updated_at", "assigned_at", "is_deleted"]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     request = self.context.get("request")
    #     if request and request.user.is_superuser and request.method == "GET":
    #         self.Meta.fields.append("created_by")
    #     else:
    #         self.Meta.read_only_fields.append("created_by")

    def create(self, validated_data):
        if "assigned_to" in validated_data:
            validated_data["assigned_at"] = datetime.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "assigned_to" in validated_data:
            validated_data["assigned_at"] = datetime.now()
        validated_data["updated_at"] = datetime.now()
        return super().update(instance, validated_data)


class TaskCommentSerializer(serializers.ModelSerializer):
    # TODO: need to add created by only for super user while fetching data
    comment_by = serializers.SerializerMethodField("get_comment_by")

    class Meta:
        model = TaskComments
        exclude = ["task_id", "is_deleted"]
        read_only_fields = ["comment_at", "comment_updated_at", "comment_by"]

    def get_comment_by(self, obj):
        if obj:
            return f"{obj.comment_by.first_name} {obj.comment_by.last_name}"

    # def update(self, instance, validated_data):
    #     print("22222")
    #     # Remove comment_at from validated_data to prevent updating it
    #     validated_data.pop("comment_at", None)
    #     return super().update(instance, validated_data)
