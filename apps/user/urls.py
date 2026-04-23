from django.urls import path
from .views import ViewsRegisterUser,ViewsLoginUser,ViewsLogout,ViewsDetailProfileMy,ViewsUpdateProfile,ViewsDetailProfile
urlpatterns = [
    path('',ViewsRegisterUser.as_view(),name='register'),
    path('login/',ViewsLoginUser.as_view(),name='login'),
    path('logout/',ViewsLogout.as_view(),name='logout'),
    path('profile/',ViewsDetailProfileMy.as_view(),name = 'detail_user_my'),
    path('profile/update/',ViewsUpdateProfile.as_view(),name='update_profile'),
    path('profile/<slug:slug>/',ViewsDetailProfile.as_view(),name="detail_user"),
]
