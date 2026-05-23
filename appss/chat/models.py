from uuid import uuid4
from django.db import models
from appss.shop.models import Service,Task
from appss.user.models import User
from .abstract import BaseOffer,BaseChat,BaseMessage

class ServiceOffer(BaseOffer):
    product = models.ForeignKey(Service,verbose_name="service",on_delete=models.CASCADE)
    class Meta():
            unique_together = ['product', 'executor']
            
class ServiceChat(BaseChat):
    offer = models.OneToOneField(ServiceOffer,on_delete=models.CASCADE)

class ServiceMessage(BaseMessage):
    chat = models.ForeignKey(ServiceChat,on_delete=models.CASCADE)

#task
class TaskOffer(BaseOffer):

    product = models.ForeignKey(Task,verbose_name="task",on_delete=models.CASCADE)
        
    class Meta():
            unique_together = ['product', 'executor']


class TaskChat(BaseChat):
    offer = models.OneToOneField(TaskOffer,on_delete=models.CASCADE)

class TaskMessage(BaseMessage):
    chat = models.ForeignKey(TaskChat,on_delete=models.CASCADE)
    
    

    
    