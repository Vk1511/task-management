from django.db import models
from jwt_auth.models import Users

"""
    Model Use: Manage User Task
    Referred from: Users
    Referred by: SharedTask, TaskComments
"""


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
    created_by = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="created_by"
    )
    assigned_to = models.ForeignKey(
        Users, on_delete=models.SET_NULL, related_name="assigned_to", null=True
    )
    assigned_at = models.DateTimeField(blank=False, null=True)
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
    # TODO: add one to many to manage document

    class Meta:
        unique_together = ("title", "created_by")

    def __str__(self):
        return f"Task {self.title} created by {self.created_by}."


"""
    Model Use: Manage Task comments
    Referred from: Users, UserTask
    Referred by: None
"""


class TaskComments(models.Model):
    task_id = models.ForeignKey(UserTask, on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
    comment_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment_at = models.DateTimeField(null=False, blank=False)
    comment_updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    # TODO: add one to manage to manage documents

    def __str__(self):
        return f"Task comment added by {self.comment_by}"

    def mark_comments_as_deleted(self):
        self.is_deleted = True
        self.save()
