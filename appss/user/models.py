import uuid
from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from pytils.translit import slugify
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True,verbose_name="Имя пользователя",help_text="Ввидите имя пользователя")
    is_staff = models.BooleanField(default=False)
    verification_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True,null=True, blank=True)

    


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
            # Берём за основу username (можно заменить на другое поле: email, first_name и т.п.)
            base_slug = slugify(self.user.username)
            slug = base_slug
            counter = 1
            # Ищем профиль с таким же slug (исключая самого себя, если он уже есть в БД)
            while Profile.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)