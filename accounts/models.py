import os
import random

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField
from django_countries.fields import CountryField

# Create your models here.

def get_filename_extention(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):

    new_filename=random.randint(1,12345)
    name,ext=get_filename_extention(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=filename,ext=ext)
    return 'realator/{new_filename}/{final_filename}'.format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Profile(models.Model):
    realator = models.OneToOneField(settings.AUTH_USER_MODEL,unique=True,related_name='realator',on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200,blank=True,null=True)
    image    = models.ImageField(upload_image_path,default='default.jpg',blank=True,null=True)
    about    =models.TextField(blank=True,null=True)
    phone    =PhoneNumberField(blank=True,null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address   = AddressField(on_delete=models.CASCADE,blank=True,null=True)
    country=CountryField(blank_label='(select country)',blank=True,null=True)

def post_save_user_receiver(sender,instance,created,*args,**kwargs):
    #user will saved as profile
    if created:
        new_profile= Profile.objects.get_or_create(realator=instance)

post_save.connect(post_save_user_receiver,sender=settings.AUTH_USER_MODEL)





