from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import (
    UserRegistrationSerializer,
    UserProfileSerializer,
    UserPasswordChangeSerializer,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileRegistrationView(generics.CreateAPIView):
    """
    To Create user based on POST request to 'user/register' endpoint
    """

    serializer_class = UserRegistrationSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()


class UserProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    To Get and Update User details
    """

    def get_object(self):
        """
        To get User object who is sending Request
        """
        return self.request.user

    def get_serializer_class(self):
        return UserProfileSerializer

    def patch(self, request):
        """
        To Update User Firstname, Lastname, DOB, Email and Phone Number.
        Niether Email nor Phone Number can be updated once verified
        """
        user_db_details = self.get_object()
        user_request_data = self.request.data
        serializer = self.get_serializer(user_db_details, data=user_request_data)
        if serializer.is_valid():
            serializer.update(user_db_details, serializer.validated_data)

            response = {}
            response["message"] = "User details Updated Successfully"
            response.update(serializer.data)

            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserChangePasswordView(generics.UpdateAPIView):
    serializer_class = UserPasswordChangeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.update(self.object, serializer.data)

            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
