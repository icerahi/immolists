
from django.contrib import admin
from django.urls import path, include

from immolists.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('properties.urls')),

]

 
