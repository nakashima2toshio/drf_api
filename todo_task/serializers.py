from rest_framework import serializers
from todo_task.models import Task

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
