from django.urls import path
from .views import (
    ViewsCreateOfferTask,
    ViewsCreateOfferService,
    ViewsListOfferTask,
    ViewsDetailChatTask,
    ViewsCreateChatTask,
    ViewsCreateTaskMessege,
    ViewsListChatTask,
    ViewsListOfferService,
    ViewsCreateChatService,
    ViewsDetailChatService,
    ViewsCreateServiceMessege,
    ViewsListChatService,
    )

urlpatterns = [
    path(
        'create_offer/service/<int:task_id>/',
        ViewsCreateOfferService.as_view(),
        name='create_service_offer'
        ),
    path('list_service/offers/<slug:service_slug>',
        ViewsListOfferService.as_view(),
        name='service_offers_task'
        ),
    path(
        'create_chat_service/<int:service_id>/',
        ViewsCreateChatService.as_view(),
        name='create_chat_service'
        ),
    path(
        'detail_chat/service/<int:chat_id>/',
        ViewsDetailChatService.as_view(),
        name='service_chat_detail'
        ),
    path(
        'create_message_service/<int:chat_id>/',
        ViewsCreateServiceMessege.as_view(),
        name='create_message_service'
        ),
    path(
        'list_service/chat/',
        ViewsListChatService.as_view(),
        name='list_service_chat'
        ),
    
    # ========== TASK ==========
    path(
        'create_offer/task/<int:task_id>/',
        ViewsCreateOfferTask.as_view(),
        name='create_task_offer'
        ),

    path(
        'list_task/offers/<slug:task_slug>/',
        ViewsListOfferTask.as_view(),
        name='list_offers_task'
        ),

    path(
        'detail_chat/task/<int:chat_id>/',
        ViewsDetailChatTask.as_view(),
        name='task_chat_detail'
        ),

    path(
        'create_chat_task/<int:offer_id>/'
        ,ViewsCreateChatTask.as_view()
        ,name='create_chat_task'
        ),

    path(
        'create_message_task/<int:chat_id>/',
        ViewsCreateTaskMessege.as_view(),
        name='create_message_task'
        ),
    
    path(
        'list_task/chat/',
        ViewsListChatTask.as_view(),
        name='list_task_chat'
        ),
]
