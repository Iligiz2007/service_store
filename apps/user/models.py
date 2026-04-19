from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True,verbose_name="Имя пользователя",help_text="Ввидите имя пользователя")
    is_staff = models.BooleanField(default=False)

    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="avatars/",
        verbose_name="Аватарка",
        default="5856.jpg"
    )
    slug = models.SlugField(max_length=255,unique=True)
    bio = models.TextField(max_length=500)
    birth_date = models.DateField(null=True,blank=True)
        
    def save(self, *args, **kwargs):
        # 1. Сначала создаем slug (ДО сохранения)
        if not self.slug:
            self.slug = slugify(self.user.username)
        
        # 2. Обрабатываем аватарку
        if self.avatar:
            try:
                avatar = Image.open(self.avatar.path)
                
                if avatar.height > 100 or avatar.width > 100:
                    new_avatar = (100, 100)
                    avatar.thumbnail(new_avatar)
                    avatar.save(self.avatar.path)
            except (AttributeError, IOError):
                # добавить позже логирование 
                pass
        
        # 3. ТОЛЬКО ТЕПЕРЬ сохраняем
        super().save(*args, **kwargs)