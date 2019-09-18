from rest_framework import serializers
from . import models

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaskList
        fields = '__all__'
