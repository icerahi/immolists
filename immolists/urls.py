from decorator_include import decorator_include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('media/<path>/', serve, {'document_root': settings.MEDIA_ROOT}),

    path('dashboard/', decorator_include(login_required,('dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include(('original_site.urls', 'original_site'), namespace='site'))
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




