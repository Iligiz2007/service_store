from django.urls import path
from .views import ViewsService,ViewsIndex

urlpatterns = [
    path('form_servace/', ViewsService.as_view(),name='form_servace_name'),
    path('',ViewsIndex.as_view(),name="home"),
]
