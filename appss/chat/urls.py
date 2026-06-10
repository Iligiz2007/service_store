from django.urls import path
from .views import (
    ViewsCreateOfferTask,
    ViewsCreateOfferService,
    ViewsListOfferTask,
    ViewsDetailChat,
    ViewsCreateChatTask,
    ViewsCreateTaskMessege,
    ViewsListChatTask
    )

urlpatterns = [
    path(
        'create_offer/task/<int:task_id>/',
        ViewsCreateOfferTask.as_view(),
        name='create_task_offer'
        ),

    path(
        'create_offer/service/<int:task_id>/',
        ViewsCreateOfferService.as_view(),
        name='create_service_offer'
        ),

    path(
        'list_task/offers/<slug:task_slug>/',
        ViewsListOfferTask.as_view(),
        name='list_offers_task'
        ),

    path(
        'detail_chat/<int:chat_id>/',
        ViewsDetailChat.as_view(),
        name='chat_detail'
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
