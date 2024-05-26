from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, APIException, PermissionDenied
from datetime import datetime
from django.db.models import Q
from .serializers import UserTaskSerializer, TaskCommentSerializer
from .models import UserTask, TaskComments


class UserTaskManageView(viewsets.ModelViewSet):
    def get_serializer_class(self):
        # if self.request.method == "GET":
        #     return GetUserTaskSerializer
        return UserTaskSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserTask.objects.filter(is_deleted=False).order_by("-created_at")
        else:
            return UserTask.objects.filter(
                created_by=self.request.user.id, is_deleted=False
            ).order_by("-created_at")

    # Need to override list method, as we are returning additonal fields along with data
    def list(self, request, *args, **kwargs):
        # TODO: Filter to fetch only public or private task
        response = {}
        user_tasks = self.get_queryset()
        serializer = self.get_serializer(user_tasks, many=True)
        response = {"total_task": len(user_tasks), "task": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # TODO pass custom error message for retrival metod


class TaskComment(generics.ListCreateAPIView):
    serializer_class = TaskCommentSerializer

    def get_queryset(self):
        task_id = self.kwargs.get("task_id")
        try:
            _ = UserTask.objects.get(id=task_id)
            return TaskComments.objects.filter(task_id=task_id).order_by("-comment_at")
        except UserTask.DoesNotExist:
            raise NotFound("Invalid task id passed.")

    def perform_create(self, serializer):
        task_id = self.kwargs.get("task_id")
        try:
            task = UserTask.objects.get(id=task_id)
            serializer.save(
                task_id=task, comment_by=self.request.user, comment_at=datetime.now()
            )
        except UserTask.DoesNotExist:
            raise NotFound("Invalid task id passed.")
        # TODO: handle other exception
        # TODO: deivide code


class TaskCommentManipulation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskCommentSerializer
    lookup_url_kwarg = "comment_id"

    def get_queryset(self):
        task_id = self.kwargs.get("task_id")
        try:
            _ = UserTask.objects.get(id=task_id)
            return TaskComments.objects.filter(
                task_id=task_id, is_deleted=False
            ).order_by("-comment_at")
        except UserTask.DoesNotExist:
            raise NotFound("Invalid task id passed.")

    def get_object(self):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            comment_id = self.kwargs.get(self.lookup_url_kwarg)
            comment = queryset.get(id=comment_id)
            if comment.comment_by != self.request.user:
                raise PermissionDenied("You are not the owner of this comment.")
            return comment
        except TaskComments.DoesNotExist:
            raise NotFound("Invalid comment id passed or comment is deleted.")

    def perform_destroy(self, instance):
        try:
            comment = self.get_object()
            comment.mark_comments_as_deleted()
            return Response(
                {"message": "Comment deleted successfully."}, status=status.HTTP_200_OK
            )
        except UserTask.DoesNotExist:
            raise NotFound("Invalid task id passed.")
