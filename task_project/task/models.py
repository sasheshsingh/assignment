from django.db import models

from task_project.task.mixins import StatusMixin, TimeStampedMixin


# Create your models here.
class TaskModel(StatusMixin, TimeStampedMixin):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
