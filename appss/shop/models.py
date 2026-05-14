from django.db import models
from django.core.validators import MinValueValidator
from appss.user.models import User
from django.utils.text import slugify
from uuid import uuid4
from django.utils import timezone 
# Create your models here.


class BaseModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="",
        help_text="")
    
    description = models.TextField(
        verbose_name="",
        help_text="")
    
    price = models.PositiveIntegerField(
        verbose_name="",
        help_text="",
        validators=[MinValueValidator(100)])
    slug = models.SlugField(max_length=255,unique=True ,blank=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{self.user.pk}"

        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
    class Meta:
        abstract = True
        unique_together = ['user', 'title']
    
    

class Service(BaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Название услуг")
    
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание ваших услуги")
    
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        help_text="Стоимость: минимально 100р",
        validators=[MinValueValidator(100)])

    
class Task(BaseModel):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Название задачи")
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание ваших задачи")
    
    price = models.PositiveIntegerField(
        verbose_name="Цена",
        help_text="Стоимость: минимально 100р",
        validators=[MinValueValidator(100)])
    

