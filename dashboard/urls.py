
from django.urls import path, include

from accounts import views
from accounts.views import PersonalInformation
from dashboard.views import CreateSellProperty, MyList, SellPropertyUpdate, SellPropertyDelete, Dashboard, load_types
from immolists.views import IndexView

urlpatterns = [
    path('mylist/', MyList.as_view(), name='mylist'),
    path('mylist/edit/<int:pk>/<slug>', SellPropertyUpdate.as_view(), name='sell_update'),
    path('mylist/delete/<int:pk>/<slug>', SellPropertyDelete.as_view(), name='sell_delete'),
    path('',Dashboard.as_view(),name='dashboard'),
    path('ajax/load-types/', load_types, name='ajax_load_types'),
    path('add_sell/',CreateSellProperty.as_view(),name='add_sell'),

    path('personal-information/<username>/',PersonalInformation.as_view(),name='personal_info'),

    path('personal-information/<username>/edit/',views.profile_edit,name='profile_edit'),






]