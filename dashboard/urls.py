
from django.urls import path, include

from dashboard.views import CreateSellProperty, MyList, SellPropertyUpdate, SellPropertyDelete
from immolists.views import IndexView

urlpatterns = [
    path('add_sell/',CreateSellProperty.as_view(),name='add_sell'),
    path('mylist/',MyList.as_view(),name='mylist'),
    path('mylist/edit/<pk>/<slug>/',SellPropertyUpdate.as_view(),name='sell_update'),
    path('mylist/delete/<pk>/<slug>/',SellPropertyDelete.as_view(),name='sell_delete'),

]
