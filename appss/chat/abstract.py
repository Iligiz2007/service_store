from uuid import uuid4
from django.db import models
from appss.shop.models import Service,Task
from appss.user.models import User

class BaseOffer(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Ожидает'
        ACCEPTED = 'accepted', 'Принят'
        REJECTED = 'rejected', 'Отклонен'

    
    executor = models.ForeignKey(User,verbose_name="executor",on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices,default=Status.PENDING)
    created_ad = models.DateTimeField(auto_now_add=True)
    proposed_price = models.PositiveIntegerField(null=True,blank=True)
    message = models.TextField(verbose_name="Сопроводительное письмо")
    
    class Meta():
        abstract = True


class BaseChat(models.Model):
    status = models.BooleanField(default=True)
    uuid = models.UUIDField(default=uuid4,editable=False)
    created_ad = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(User)
    
    class Meta:
        abstract = True


class BaseMessage(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    def __str__(self) -> str:
        date = self.timestamp.date()
        time = self.timestamp.time()
        return f"{self.author}:- {self.content} @{date} {time.hour}:{time.minute}"