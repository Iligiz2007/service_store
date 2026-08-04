from django.urls import path
from .views import (
    ViewsService,
    ViewsIndex,
    ViewsListService,
    ViewsDetialService,
    ViewsUserListService,
    ViewsUpdateService,
    ViewsFormTask,
    ViewsListTaskMy,
    ViewsDetailTask,
    ViewsUpdateTask,
    ViewsListTask,
    ViewsHTMXListMyTask,
    ViewsHTMXListMyService,
    )
app_name = 'shop'
urlpatterns = [
    path(
        'list_service/',
        ViewsListService.as_view(),
        name='list_service'
         ),
         
    path(
        'list_task_my/',
        ViewsListTaskMy.as_view(),
        name='list_task_my'
        ),

    path(
        'list_task/',
        ViewsListTask.as_view(),
        name='list_task'
        ),

    path(
        'form_servace/',
        ViewsService.as_view(),
        name='form_servace_name'
        ),

    path(
        "list_service_my/",
        ViewsUserListService.as_view(),
        name="list_service_my"
        ),
        
    path(
        'create_task/',
        ViewsFormTask.as_view(),
        name='create_task'
        ),

    path(
        '',ViewsIndex.as_view()
        ,name="home"
        ),

    path(
        'update/task/<slug:slug>',
        ViewsUpdateTask.as_view(),
        name='update_task'
        ),

    path(
        'detail_servase/<slug:slug>/',
         ViewsDetialService.as_view(),
         name="detail_service"
         ),
         
    path(
        "update/service/<slug:slug>",
        ViewsUpdateService.as_view(),
        name="update_service"
        ),

    path(
        'detail_task/<slug:slug>/',
        ViewsDetailTask.as_view(),
        name='detail_task'
        ),
    #TASK
    path(
        'htmx_listtask',
        ViewsHTMXListMyTask.as_view(),
        name="list_htmx_task"
        ),
    #SERVICE
        path(
        'htmx_listservice',
        ViewsHTMXListMyService.as_view(),
        name="list_htmx_service"
        ),
]
