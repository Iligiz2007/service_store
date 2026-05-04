from django.urls import path
from .views import ViewsOffers
urlpatterns = [
    path('offer/',ViewsOffers.as_view(),name='create_offer')
]
