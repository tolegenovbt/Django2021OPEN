from rest_framework import serializers
from main.models import List, Task


class ListSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['name']


class ListSerializerFull(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'


class TaskSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'mark']


class TaskSerializerFull(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
