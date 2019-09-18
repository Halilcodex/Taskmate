from rest_framework import serializers
from . import models

class TaskListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TaskList
        fields = '__all__'
