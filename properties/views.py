from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from properties.forms import PropertyForSellForm
from properties.models import PropertyForSell, Type


class PropertyListView(ListView):
    model=PropertyForSell
    context_object_name='property'
    template_name = 'property_list.html'



class PropertyCreateView(CreateView,LoginRequiredMixin):
    model=PropertyForSell
    form_class = PropertyForSellForm
    success_url = reverse_lazy('property_list')
    template_name = 'sell_property.html'

    def form_valid(self, form):
        form=PropertyForSellForm(self.request.POST,self.request.FILES)
        form.instance.realator=self.request.user
        return super(PropertyCreateView, self).form_valid(form)

class PropertyUpdateView(UpdateView,LoginRequiredMixin):
    model=PropertyForSell
    success_url = reverse_lazy('property_list')
    form_class = PropertyForSellForm
    template_name = 'sell_property.html'

class PropertyDetailView(DetailView):
    model = PropertyForSell
    template_name = 'property_detail.html'

class PropertyDeleteView(DeleteView):
    model = PropertyForSell
    template_name = 'property_delete.html'
    success_url = reverse_lazy('property_list')

def load_types(request):
    category_id=request.GET.get('category')
    types=Type.objects.filter(category_id=category_id).order_by('name')
    return render(request,'type_dropdown_list.html',{'types':types})




