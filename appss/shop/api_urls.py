from django.urls import path
from .api_views import TaskViewSet
urlpatterns = [
    path('',TaskViewSet.as_view(),name="api_task"),
]