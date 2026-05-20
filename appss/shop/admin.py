from django.contrib import admin
from .models import Service,Task
# Register your models here.

@admin.register(Service)
class AdminServise(admin.ModelAdmin):
    fields = ['title','description','slug','price','user']
@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    fields = ['title','description','slug','price','user']
