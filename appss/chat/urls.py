from django.urls import path
from .views import ViewsCreateOffer

urlpatterns = [
    path('create_offer/<int:task_id>/',ViewsCreateOffer.as_view(),name='create_task_offer'),
]
