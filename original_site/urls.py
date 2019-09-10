from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('home/',views.Home.as_view(),name='home'),
    path('<pk>/<slug>/',views.PropertyDetailView,name='detail'),
]


