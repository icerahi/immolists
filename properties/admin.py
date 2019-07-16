from django.contrib import admin
from django.db import models


from .models import Category,Type,PropertyForSell
# Register your models here
admin.site.register(Category)
admin.site.register(Type)



admin.site.register(PropertyForSell)