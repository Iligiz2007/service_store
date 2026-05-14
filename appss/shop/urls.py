from django.urls import path
from .views import ViewsService,ViewsIndex,ViewsListService,ViewsDetialService,ViewsUserListService,ViewsUpdateService
app_name = 'shop'
urlpatterns = [
    path('detail_servase/<slug:slug>/',ViewsDetialService.as_view(),name="detail_service"),
    path('list_service/',ViewsListService.as_view(),name='list_service'),
    path('form_servace/', ViewsService.as_view(),name='form_servace_name'),
    path("list_service_my/", ViewsUserListService.as_view(), name="list_service_my"),
    path("update/service/<slug:slug>", ViewsUpdateService.as_view(), name="update_service"),
    path('',ViewsIndex.as_view(),name="home"),
]
