from uuid import uuid4
from django.db import models
from apps.shop.models import Service
from apps.user.models import User


class Offer(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Ожидает'
        ACCEPTED = 'accepted', 'Принят'
        REJECTED = 'rejected', 'Отклонен'

    
    service = models.ForeignKey(Service,verbose_name="service",on_delete=models.CASCADE)
    executor = models.ForeignKey(User,verbose_name="executor",on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices,default=Status.PENDING)
    create_ad = models.DateTimeField(auto_now_add=True)
    proposed_price = models.PositiveIntegerField(null=True,blank=True)
    messege = models.TextField(verbose_name="Сопроводительное письмо")
    
    class Meta():
        unique_together = ['service', 'executor']
        

class Chat(models.Model):
    status = models.BooleanField(default=True)
    uuid = models.UUIDField(default=uuid4,editable=False)
    create_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    members = models.ManyToManyField(User)
    offer = models.OneToOneField(Offer,on_delete=models.CASCADE)

class Message(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    
    
    def __str__(self) -> str:
        date = self.timestamp.date()
        time = self.timestamp.time()
        return f"{self.author}:- {self.content} @{date} {time.hour}:{time.minute}"
    