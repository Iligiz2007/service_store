from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)