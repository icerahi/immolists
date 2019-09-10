
from django.urls import path, include

from accounts import views
from accounts.views import PersonalInformation
from dashboard.views import CreateSellProperty, MyList, SellPropertyUpdate, SellPropertyDelete, Dashboard, load_types, \
    EnquiryCome, EnquirySend, EnquiryComeDelete, EnquirySendDelete, favourite, FavouriteList, remove_favourite
from immolists.views import IndexView



urlpatterns = [
    path('remove_favourite/<int:pk>/',remove_favourite,name='remove_favourite'),
    path('myfavourite/',FavouriteList.as_view(),name='favourite_list'),
    path('add_favourite/<int:pk>/',favourite,name='add_favourite'),
    path('enquiry_send/delete/<int:pk>/', EnquirySendDelete.as_view(), name='enquirysend_delete'),
    path('enquiry_send/',EnquirySend.as_view(),name='enquiry_send'),
    path('enquiry_come/delete/<int:pk>/', EnquiryComeDelete.as_view(), name='enquirycome_delete'),
    path('enquiry_come/',EnquiryCome.as_view(),name='enquiry_come'),
    path('mylist/', MyList.as_view(), name='mylist'),
    path('mylist/edit/<int:pk>/<slug>', SellPropertyUpdate.as_view(), name='sell_update'),
    path('mylist/delete/<int:pk>/<slug>', SellPropertyDelete.as_view(), name='sell_delete'),
    path('',Dashboard.as_view(),name='dashboard'),
    path('ajax/load-types/', load_types, name='ajax_load_types'),
    path('add_sell/',CreateSellProperty.as_view(),name='add_sell'),

    path('personal-information/<username>/',PersonalInformation.as_view(),name='personal_info'),

    path('personal-information/<username>/edit/',views.profile_edit,name='profile_edit'),







]
