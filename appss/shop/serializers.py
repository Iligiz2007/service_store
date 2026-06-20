from rest_framework import serializers
from .models import(
    Task,
    Service,
        )

class TaskSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Task
        fields = ('title','description','price','username',)



class ServiceSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Service
        fields = ('title','description','price','username',)