from django.contrib import admin
from .models import * 
# Register your models here.
@admin.register(TaskOffer)
class TaskOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'executor', 'customer', 'status')

    def customer(self, obj):
        return obj.product.user

@admin.register(ServiceOffer)
class ServiceOfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'executor', 'customer', 'status')

    def customer(self, obj):
        return obj.product.user

admin.site.register(TaskChat)