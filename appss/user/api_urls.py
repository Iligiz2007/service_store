from django.urls import include, path
from .api_views import  UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users',UserViewSet)



urlpatterns = [
    path('', include(router.urls)),
]