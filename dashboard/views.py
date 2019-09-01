from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView

from sellproperty.forms import SellPropertyForm
from sellproperty.models import SellProperty, Type

class Dashboard(TemplateView):
    template_name = 'dashboard_base.html'


class CreateSellProperty(CreateView,LoginRequiredMixin):
    model=SellProperty
    form_class = SellPropertyForm
    template_name = 'sell.html'
    success_url = reverse_lazy('dashboard:mylist')

    def form_valid(self, form):
        form=SellPropertyForm(self.request.POST,self.request.FILES)
        form.instance.realator=self.request.user
        return super(CreateSellProperty, self).form_valid(form)





def load_types(request):
    category_id=request.GET.get('category')
    types=Type.objects.filter(category_id=category_id).order_by('name')
    return render(request,'type_dropdown_list.html',{'types':types})

class MyList(ListView,LoginRequiredMixin):
    model = SellProperty
    template_name = 'mylist.html'

    def get_queryset(self,*args,**kwargs):
        queryset=SellProperty.objects.all()
        queryset=queryset.filter(realator=self.request.user)
        return queryset

class SellPropertyUpdate(UpdateView,LoginRequiredMixin):
    model = SellProperty
    form_class = SellPropertyForm
    template_name = 'sell.html'
    success_url = reverse_lazy('dashboard:mylist')

class SellPropertyDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model=SellProperty()
    success_url =reverse_lazy('dashboard:mylist')
    success_message = "Property Deleted Successfully"



