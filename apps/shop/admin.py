from django.contrib import admin
from .models import Offer,Service
# Register your models here.
@admin.register(Offer)
class UserOffer(admin.ModelAdmin):
    fields = ['service', 'executor', 'proposed_price', 'messege']

@admin.register(Service)
class ModelServise(admin.ModelAdmin):
    fields = ['title','description','price','user']