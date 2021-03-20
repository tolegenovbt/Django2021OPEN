from rest_framework import serializers
from .models import MainUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
