from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200,unique=True,)

    def __str__(self):
        return f"{self.name}"

class Type(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"



class PropertyForSell(models.Model):
    realator=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    type=models.ForeignKey(Type,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)


    def __str__(self):
        return f"{self.title}"
