from django.urls import path
from .views import ViewsRegisterUser,ViewsLoginUser,ViewsLogout,ViewsDetailUser,ViewsUpdateProfile
urlpatterns = [
    path('',ViewsRegisterUser.as_view(),name='register'),
    path('login/',ViewsLoginUser.as_view(),name='login'),
    path('logout/',ViewsLogout.as_view(),name='logout'),
    path('profile/update/',ViewsUpdateProfile.as_view(),name='update_profile'),
    path('profile/<slug:slug>/',ViewsDetailUser.as_view(),name="detail_user"),
]
