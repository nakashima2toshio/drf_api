from rest_framework import serializers
from todo_task.models import TodoTask

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = '__all__'
