from appss.shop.models import Task

from rest_framework.viewsets import ModelViewSet
from .serializers import TaskOfferSerializer
from .models import TaskOffer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

class TaskOfferViewSet(ModelViewSet):
    serializer_class = TaskOfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем оферы только для конкретной задачи, и только владельцу задачи
        task_id = self.kwargs.get('task_pk')  # если используешь nested routers
        return TaskOffer.objects.filter(product_id=task_id, product__user=self.request.user)

    def perform_create(self, serializer):
        # Подставляем исполнителя и задачу
        task = get_object_or_404(Task, id=self.kwargs['task_pk'])
        if task.user == self.request.user:
            raise PermissionDenied("Нельзя предлагать самому себе")
        serializer.save(executor=self.request.user, product=task)