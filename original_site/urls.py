from django.urls import path
from . import views

urlpatterns = [
    path('sell_list/',views.SellList.as_view(),name='sell_list'),
    path('realators/',views.RealatorList.as_view(),name='realators'),
    path('',views.Home.as_view(),name='home'),
    path('home/',views.Home.as_view(),name='home'),
    path('<pk>/<slug>/',views.PropertyDetailView,name='detail'),
    path('<username>/',views.ProfileView.as_view(),name='profile'),
]


