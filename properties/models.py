from django.conf import settings
from django.db import models




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

class PropertyForSell(models.Model):
    STATUS_CHOICES=(
        ('draf','Draft'),
        ('published','Published')
    )
    realator         =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,default=None)
    category         =models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    type             =models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    title            =models.CharField(max_length=200)
    full_description =models.TextField()
    key_features     =models.TextField()
    min_price        =models.IntegerField()
    max_price        =models.IntegerField()
    created          =models.DateTimeField(auto_now_add=True)
    updated          =models.DateTimeField(auto_now=True)
    slug             = models.SlugField()
    saved            =models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='saved')
    status           =models.CharField(max_length=12,choices=STATUS_CHOICES,default='published')
    published        =PublishedManager() #Costom model manager
    location         =models.CharField(max_length=200)
    google_map       =models.URLField()


    def __str__(self):
        return f"{self.title}"


