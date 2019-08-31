from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from immolists.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('properties.urls')),
    path('dashboard/',include(('dashboard.urls','dashboard'),namespace='dashboard')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('account/', include('allauth.urls')),

]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

 
