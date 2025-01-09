from rest_framework import serializers
from .models import TaskList


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = TaskList
        fields = '__all__'
