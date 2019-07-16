from django.urls import path
from . import views

urlpatterns = [
    path('',views.PropertyListView.as_view(),name='property_list'),
    path('add/',views.PropertyCreateView.as_view(),name='property_add'),
    path('<int:pk>/<slug>',views.PropertyDetailView.as_view(),name='property_detail'),
    path('update/<int:pk>/<slug>',views.PropertyUpdateView.as_view(),name='property_update'),
    path('delete/<int:pk>/<slug>',views.PropertyDeleteView.as_view(),name='property_delete'),
    path('ajax/load-types/',views.load_types,name='ajax_load_types'),

]


