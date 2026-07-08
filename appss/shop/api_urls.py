from django.urls import include, path
from .api_views import TaskViewSet,ServiceViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'tasks',TaskViewSet)
router.register(r'services',ServiceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]