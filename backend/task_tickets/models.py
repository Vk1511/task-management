from django.db import models
from jwt_auth.models import Users


class UserTask(models.Model):
    class TaskPriority(models.TextChoices):
        HIGH = "HIGH", "High"
        MEDIUM = "MEDIUM", "Medium"
        LOW = "LOW", "Low"

    class TaskStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN PROGRESS", "In Progress"
        DONE = "DONE", "Done"

    title = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=8, choices=TaskPriority.choices, default=TaskPriority.LOW
    )
    due_date = models.DateTimeField(blank=False)
    status = models.CharField(
        max_length=16, choices=TaskStatus.choices, default=TaskStatus.PENDING
    )
    is_public = models.BooleanField(default=True)

    """
        is_deleted: to manage the deletion of task.
        we will not delete the task when user want to delete it. we just mark it as inactive.
        after a month, we can delete all the task who are marked as inactive.
        This will help us in data recovery, if user by mistakly deletes the task
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Mets:
        unique_together = ("title", "created_by")

    def __str__(self):
        return self.name
