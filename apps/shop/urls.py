from django.urls import path
from .views import ViewsService,ViewsIndex,ViewsListService

urlpatterns = [
    path('list_service/',ViewsListService.as_view(),name='list_service'),
    path('form_servace/', ViewsService.as_view(),name='form_servace_name'),
    path('',ViewsIndex.as_view(),name="home"),
]
