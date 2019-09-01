from django.urls import path
from . import views

urlpatterns = [
    #path('home/',views.PropertyListView.as_view(),name='property_list'),
   # path('add/',views.PropertyCreateView.as_view(),name='property_add'),
    path('<int:pk>/<slug>',views.PropertyDetailView.as_view(),name='property_detail'),
    #path('update/<int:pk>/<slug>',views.PropertyUpdateView.as_view(),name='property_update'),
    #path('delete/<int:pk>/<slug>',views.PropertyDeleteView.as_view(),name='property_delete'),
    #path('ajax/load-types/',views.load_types,name='ajax_load_types'),

        #check dashboard templates
    path('dashboard/',views.CheckTemplate.as_view(),name='dashboard'),
    path('send/',views.EnquireSend.as_view(),name='send'),
    path('come/',views.EnquireCome.as_view(),name='come'),
    path('list/',views.MyList.as_view(),name='list'),
    path('favourite/',views.FavouriteList.as_view(),name='favourite'),
    path('offer/',views.OfferList.as_view(),name='offer'),
    path('personalinfo/',views.PersonalInfo.as_view(),name='personalinfo'),
    path('password_change/',views.PasswordChange.as_view(),name='password_change'),
    path('sell/',views.Sell.as_view(),name='sell'),
    path('rent/',views.Rent.as_view(),name='rent'),
    path('make_offer/',views.MakeOffer.as_view(),name='make_offer'),

    ## check actual site templates
    path('',views.Home.as_view(),name='home'),
    path('search/',views.Search,name='search'),
    path('comming_soon/',views.CommingSoon.as_view(),name='comming_soon'),
    path('agent_list/',views.AgentList.as_view(),name='agent_list'),
    path('about_agent/',views.AboutAgent.as_view(),name='about_agent'),
    path('property_list/',views.PropertyList.as_view(),name='property_list'),
    path('single/',views.single.as_view(),name='single'),
    path('faq/',views.faq.as_view(),name='faq'),
    path('register/',views.register.as_view(),name='register'),
    path('login/',views.login.as_view(),name='login'),
    path('forget_password/',views.forget_password.as_view(),name='forget_password'),
    path('error/',views.error.as_view(),name='error'),
    path('contact/',views.contact.as_view(),name='contact'),


]


