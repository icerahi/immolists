from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from properties.forms import PropertyForSellForm
from properties.models import PropertyForSell, Type


class PropertyListView(ListView):
    model=PropertyForSell
    context_object_name='property'
    template_name = 'property_list.html'

class PropertyCreateView(CreateView):
    model=PropertyForSell
    form_class = PropertyForSellForm
    success_url = reverse_lazy('property_list')

    template_name = 'property_create.html'

class PropertyUpdateView(UpdateView):
    model=PropertyForSell
    success_url = reverse_lazy('property_list')
    form_class = PropertyForSellForm
    template_name = 'property_create.html'

def load_types(request):
    category_id=request.GET.get('category')
    types=Type.objects.filter(category_id=category_id).order_by('name')
    return render(request,'type_dropdown_list.html',{'types':types})




