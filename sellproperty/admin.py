from django.contrib import admin

# Register your models here.
from sellproperty.models import SellProperty, Type, Category,Enquiry

admin.site.register(SellProperty)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Enquiry)
