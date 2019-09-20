from django.urls import path
from . import views

urlpatterns = [
    path('offer_for_rent/',views.OfferForRent.as_view(),name='offer_for_rent'),
    path('offer_for_sell/',views.OfferForSell.as_view(),name='offer_for_sell'),
    path('rent_list/',views.RentList.as_view(),name='rent_list'),
    path('sell_list/',views.SellList.as_view(),name='sell_list'),
    path('realators/',views.RealatorList.as_view(),name='realators'),
    path('',views.Home.as_view(),name='home'),
    path('home/',views.Home.as_view(),name='home'),
    path('<pk>/<slug>/',views.PropertyDetailView,name='detail'),
    path('<username>/',views.ProfileView.as_view(),name='profile'),
]


