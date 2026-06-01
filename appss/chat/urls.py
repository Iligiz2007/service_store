from django.urls import path
from .views import ViewsCreateOfferTask,ViewsCreateOfferService,ViewsListOfferTask

urlpatterns = [
    path('create_offer/task/<int:task_id>/',ViewsCreateOfferTask.as_view(),name='create_task_offer'),
    path('create_offer/service/<int:task_id>/',ViewsCreateOfferService.as_view(),name='create_service_offer'),
    path('list_task/offers/<slug:task_slug>/', ViewsListOfferTask.as_view(), name='list_offers_task'),
]
