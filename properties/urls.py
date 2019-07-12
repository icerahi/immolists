from django.urls import path
from . import views

urlpatterns = [
    path('',views.PropertyListView.as_view(),name='property_list'),
    path('add/',views.PropertyCreateView.as_view(),name='property_add'),
    path('<int:pk>/',views.PropertyUpdateView.as_view(),name='property_update'),
    path('ajax/load-types/',views.load_types,name='ajax_load_types'),

]


