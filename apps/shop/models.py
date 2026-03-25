from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Назоваите ваш вид услуг")
    
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание ваших услуг")
    
    price = models.IntegerField (
        verbose_name="Цена",
        help_text="Стоимость",
        validators=[MinValueValidator(100)])
    

