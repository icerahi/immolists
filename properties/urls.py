from django.urls import path
from . import views

urlpatterns = [
    path('',views.PropertyListView.as_view(),name='property_list'),
    path('add/',views.PropertyCreateView.as_view(),name='property_add'),
    path('<int:pk>/<slug>',views.PropertyDetailView.as_view(),name='property_detail'),
    path('update/<int:pk>/<slug>',views.PropertyUpdateView.as_view(),name='property_update'),
    path('delete/<int:pk>/<slug>',views.PropertyDeleteView.as_view(),name='property_delete'),
    path('ajax/load-types/',views.load_types,name='ajax_load_types'),
        #check
    path('dashboard/',views.CheckTemplate.as_view(),name='dashboard'),
    path('send/',views.EnquireSend.as_view(),name='send'),
    path('come/',views.EnquireCome.as_view(),name='come'),
    path('list/',views.PropertyList.as_view(),name='list'),
    path('favourite/',views.FavouriteList.as_view(),name='favourite'),
    path('offer/',views.OfferList.as_view(),name='offer'),
    path('personalinfo/',views.PersonalInfo.as_view(),name='personalinfo'),
    path('password_change/',views.PasswordChange.as_view(),name='password_change'),
    path('sell/',views.Sell.as_view(),name='sell'),
    path('rent/',views.Rent.as_view(),name='rent'),
    path('make_offer/',views.MakeOffer.as_view(),name='make_offer'),


]


