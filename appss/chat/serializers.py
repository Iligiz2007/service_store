from rest_framework import serializers
from . models import TaskOffer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TaskOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskOffer
        fields = '__all__'
        extra_kwargs = {
            'status': {'read_only': True}
        }