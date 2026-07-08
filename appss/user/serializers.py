from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(source='profile.avatar')
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'avatar', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }