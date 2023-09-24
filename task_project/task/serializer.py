from rest_framework import serializers

from task_project.task.models import TaskModel


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
