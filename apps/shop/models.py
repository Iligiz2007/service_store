from django.db import models
from django.core.validators import MinValueValidator
from apps.user.models import User
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
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    

