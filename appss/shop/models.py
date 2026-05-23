from django.db import models
from django.core.validators import MinValueValidator
from appss.user.models import User
from pytils.translit import slugify
from uuid import uuid4
from django.utils import timezone 
# Create your models here.


class BaseModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Название")
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание ваших задачи")
    price = models.PositiveIntegerField(
        verbose_name="",
        help_text="",
        validators=[MinValueValidator(100)])
    slug = models.SlugField(max_length=255,unique=True ,blank=True)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug
            
            counter = 1
            while self.__class__.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.title}'
    class Meta:
        abstract = True  
        unique_together = ['user', 'title']

class Service(BaseModel):

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    

    
class Task(BaseModel):
    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

