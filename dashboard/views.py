from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy, resolve
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView

from sellproperty.forms import SellPropertyForm
from sellproperty.models import SellProperty, Type, Enquiry


class Dashboard(TemplateView):
    template_name = 'dashboard_base.html'


class CreateSellProperty(CreateView,LoginRequiredMixin):
    login_url = '/login'
    redirect_field_name = 'next'
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
    model=SellProperty
    success_url =reverse_lazy('dashboard:mylist')
    success_message = "Property Deleted Successfully"


# get queryset in template
class EnquiryCome(ListView,LoginRequiredMixin):
    model = Enquiry
    template_name = 'enquiry_come.html'

    def get_queryset(self,*args,**kwargs):
        queryset=Enquiry.objects.get_come(self.request.user)
        return queryset

class EnquirySend(ListView,LoginRequiredMixin):
    model = Enquiry
    template_name = 'enquiry_send.html'

    def get_queryset(self,*args,**kwargs):
        queryset=Enquiry.objects.get_send(self.request.user)
        print(queryset)
        return queryset

class  EnquiryComeDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model=Enquiry

    success_message = "Enquiry Deleted Successfully"

    def get_success_url(self):
        return reverse('dashboard:enquiry_come')

class  EnquirySendDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model=Enquiry

    success_message = "Enquiry Deleted Successfully"

    def get_success_url(self):
        return reverse('dashboard:enquiry_send')


# add to favorite
@login_required
def favourite(request,pk):
    property=get_object_or_404(SellProperty,pk=pk)
    if property.favourite.filter(id=request.user.id).exists():
        property.favourite.remove(request.user)

    else:
        property.favourite.add(request.user)
    return redirect(property.get_absolute_url())

@login_required
def remove_favourite(request,pk):
    property=get_object_or_404(SellProperty,pk=pk)
    if property.favourite.filter(id=request.user.id).exists():
        property.favourite.remove(request.user)
    return redirect('dashboard:favourite_list')

class FavouriteList(ListView,LoginRequiredMixin):
    model = SellProperty
    template_name = 'favourite_list.html'

    def get_queryset(self):
        queryset=SellProperty.objects.all()
        queryset=queryset.filter(favourite=self.request.user)
        return queryset


class CreateRentProperty(TemplateView,LoginRequiredMixin):
    template_name = 'rent.html'

class MakeOffer(TemplateView,LoginRequiredMixin):
    template_name = 'make_offer.html'

class OfferList(TemplateView,LoginRequiredMixin):
    template_name = 'offer_list.html'




