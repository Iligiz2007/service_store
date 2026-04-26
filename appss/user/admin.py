from django.contrib import admin
from .models import User, Profile
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'password')

@admin.register(Profile)
class UserProvile(admin.ModelAdmin):
    fields = ('user','avatar','bio','birth_date')
    