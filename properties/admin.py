from django.contrib import admin
from django.db import models
from pagedown.widgets import  AdminPagedownWidget
from .models import Category,Type,PropertyForSell
# Register your models here
admin.site.register(Category)
admin.site.register(Type)

@admin.register(PropertyForSell)
class PropertyForSellAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField:{'widget':AdminPagedownWidget}
    }