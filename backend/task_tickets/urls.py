from rest_framework.routers import DefaultRouter

from django.urls import path
from .views import UserTaskManageView, TaskComment, TaskCommentManipulation

router = DefaultRouter()
router.register("", UserTaskManageView, basename="user_task_management")
urlpatterns = router.urls

urlpatterns.extend(
    [
        path(
            "<int:task_id>/comment",
            TaskComment.as_view(),
            name="add-read-comment",
        ),
        path(
            "<int:task_id>/comment/<int:comment_id>",
            TaskCommentManipulation.as_view(),
            name="update-delete-comment",
        ),
    ]
)
