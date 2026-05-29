from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from pytils.translit import slugify
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
    is_verified = models.BooleanField(default=False)
    status = models.BooleanField(default=False,blank=False,null=False)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        
       
        if self.avatar:
            try:
                avatar = Image.open(self.avatar.path)
                
                if avatar.height > 100 or avatar.width > 100:
                    new_avatar = (100, 100)
                    avatar.thumbnail(new_avatar)
                    avatar.save(self.avatar.path)
            except (AttributeError, IOError):
            
                pass
        
        
        super().save(*args, **kwargs)