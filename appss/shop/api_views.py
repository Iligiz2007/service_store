from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Task,Service
from .serializers import TaskSerializer,ServiceSerializer
from rest_framework.response import Response

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)