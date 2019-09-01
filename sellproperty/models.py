import os
import random

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify



class Category(models.Model):
    name=models.CharField(max_length=200,unique=True,)

    def __str__(self):
        return f"{self.name}"

class Type(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class AllObjectManager(models.Manager):
    def get_queryset(self):
        return super(AllObjectManager, self).get_queryset()



def get_filename_extention(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

def upload_image_path(instance,filename):

    new_filename=random.randint(1,1234567876543211)
    name,ext=get_filename_extention(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=filename,ext=ext)
    return 'sellproperty/{new_filename}/{final_filename}'.format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class SellProperty(models.Model):
    STATUS_CHOICES=(
        ('draf','Draft'),
        ('published','Published')
    )
    realator         = models.ForeignKey(User,on_delete=models.CASCADE)
    category         =models.ForeignKey(Category,on_delete=models.CASCADE)
    type             =models.ForeignKey(Type,on_delete=models.CASCADE)
    title            =models.CharField(max_length=200)
    full_description =RichTextUploadingField()
    key_features     =RichTextField()
    min_price        =models.IntegerField()
    max_price        =models.IntegerField()
    created          =models.DateTimeField(auto_now_add=True)
    updated          =models.DateTimeField(auto_now=True)
    slug             = models.SlugField()
    status           =models.CharField(max_length=12,choices=STATUS_CHOICES,default='published')
    published        =PublishedManager() #Costom model manager
    objects          =AllObjectManager() # Costom model manager
    location         =models.CharField(max_length=200)
    google_map       =models.URLField()
    main_image       =models.ImageField(upload_to=upload_image_path,default='default.jpg')
    image_2          =models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    image_3          =models.ImageField(upload_to=upload_image_path,null=True,blank=True)


    def __str__(self):
        return f"{self.title}"
    class Meta:
        ordering=['-created']

    def get_update_url(self,*args,**kwargs):
        return reverse('dashboard:sell_update',kwargs={'pk':self.pk,'slug':self.slug})

    def get_delete_url(self,*args,**kwargs):
        return reverse('dashboard:sell_delete',kwargs={'pk':self.pk,'slug':self.slug})

    def get_absolute_url(self,*args,**kwargs):
        return reverse('site:detail',kwargs={'pk':self.pk,'slug':self.slug})


@receiver(pre_save,sender=SellProperty)
def pre_save_slug(sender,**kwargs):
    slug=slugify(kwargs['instance'].title)
    kwargs['instance'].slug=slug
