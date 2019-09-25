
from django.urls import path

from . import views

urlpatterns = [
    path('base_test/',views.BaseTest.as_view(),name='base_test'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('privacy_policy/',views.Privacy.as_view(),name='privacy'),
    path('terms_and_conditions/',views.Terms.as_view(),name='terms'),
    path('faq/',views.Faq.as_view(),name='faq'),
    path('search/',views.Search,name='search'),
    path('offer_for_rent/',views.OfferForRent.as_view(),name='offer_for_rent'),
    path('offer_for_sell/',views.OfferForSell.as_view(),name='offer_for_sell'),
    path('rent_list/',views.RentList.as_view(),name='rent_list'),
    path('sell_list/',views.SellList.as_view(),name='sell_list'),
    path('realators/',views.RealatorList.as_view(),name='realators'),
    path('',views.Home.as_view(),name='home'),
    path('home/',views.Home.as_view(),name='home'),
    path('<int:pk>/<slug>/',views.PropertyDetail,name='detail'),
    path('<username>/',views.ProfileView.as_view(),name='profile'),




]
