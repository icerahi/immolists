from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from sellproperty.models import SellProperty


class Home(ListView):
    template_name = 'site/home.html'
    model = SellProperty

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        object_list = SellProperty.published.all()
        context['object_list'] = object_list
        return context


class PropertyDetailView(DetailView):
    model = SellProperty
    template_name = 'site/detail_view.html'
