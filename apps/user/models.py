from django.db import models
from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True,verbose_name="Имя пользователя",help_text="Ввидите имя пользователя")
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="user_img/%Y/%m/%d/",validators=[FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'png'))],default='5856.jpg',verbose_name="Аватарка")



    def save(self,*args,**kwargs):
        if self.avatar:
            try:
                avatar = Image.open(self.avatar.path)
                
                if avatar.height >100 or avatar.width >100:
                    new_avatar = (100,100)
                    avatar.thumbnail(new_avatar)
                    avatar.save(self.avatar.path)

            except(AttributeError,IOError):
                # добавить позже логирвание 
                pass
        super().save(*args, **kwargs)
    


