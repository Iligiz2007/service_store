from django.db import models
from django.core.validators import MinValueValidator
from apps.user.models import User
from django.utils.text import slugify
# Create your models here.

class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Название услуг")
    
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание ваших услуг")
    
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        help_text="Стоимость: минимально 100р",
        validators=[MinValueValidator(100)])
    slug = models.SlugField(max_length=255,unique=True ,blank=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{self.user.pk}"

        super().save(*args, **kwargs)
    class Meta():
        unique_together = ['user', 'title']
        


    

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
        

