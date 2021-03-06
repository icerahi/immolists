
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy, resolve
from django.views import View

from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView


from sellproperty.forms import SellPropertyForm, MakeOfferForm
from sellproperty.models import SellProperty, Type, Enquiry, MakeOffer

#dashboard
class Dashboard(View):
    def get(self,request):
        total_property=SellProperty.objects.filter(realator=self.request.user).count()
        total_sale=SellProperty.objects.filter(action='sale',realator=self.request.user).count()
        total_rent=SellProperty.objects.filter(action='rent',realator=self.request.user).count()
        total_offer=MakeOffer.objects.filter(property__realator=self.request.user).count()
        recent_properties=SellProperty.objects.filter(realator=self.request.user)[:5]
        recent_enquiy=Enquiry.objects.get_come(user=request.user)[:5]

        total_favourite=SellProperty.objects.filter(favourite=request.user).count()
        total_published=SellProperty.objects.filter(status='published').count()
        total_draft=SellProperty.objects.filter(status='draft').count()
        total_views=SellProperty.objects.filter(realator=request.user).aggregate(Sum('views'))
        total_views=total_views['views__sum']


        context={
            'total_property':total_property,
            'total_sale':total_sale,
            'total_rent':total_rent,
            'total_offer':total_offer,
            'recent_properties':recent_properties,
            'recent_enquiry':recent_enquiy,
            'total_favourite':total_favourite,
            'total_published':total_published,
            'total_draft':total_draft,
            'total_views':total_views,
        }
        return render(request,'dashboard.html',context)


#create property
class CreateSellProperty(CreateView,LoginRequiredMixin,SuccessMessageMixin):
    login_url = '/login'
    redirect_field_name = 'next'
    model=SellProperty
    form_class = SellPropertyForm
    template_name = 'sell.html'
    success_url = reverse_lazy('dashboard:mylist')
    success_message = 'Your Property Created Successfully !'

    def form_valid(self, form):
        form=SellPropertyForm(self.request.POST,self.request.FILES)
        form.instance.realator=self.request.user
        return super(CreateSellProperty, self).form_valid(form)




# for load category on type dependency dropdown
def load_types(request):
    category_id=request.GET.get('category')
    types=Type.objects.filter(category_id=category_id).order_by('name')
    return render(request,'type_dropdown_list.html',{'types':types})

#property list
class MyList(ListView,LoginRequiredMixin):
    model = SellProperty
    template_name = 'mylist.html'

    def get_queryset(self,*args,**kwargs):
        queryset=SellProperty.objects.all()
        queryset=queryset.filter(realator=self.request.user)
        return queryset

#property edit
class SellPropertyUpdate(UpdateView,LoginRequiredMixin,SuccessMessageMixin):
    model = SellProperty
    form_class = SellPropertyForm
    template_name = 'sell.html'

    def get_success_url(self):
        messages.success(self.request,'Your Property Update successfully!')
        return reverse('dashboard:mylist')

#property edit
class SellPropertyDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model=SellProperty

    def get_success_url(self):
        messages.success(self.request,"Your Property Deleted Successfully!")
        return reverse('dashboard:mylist')


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
        return queryset

class  EnquiryComeDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model=Enquiry


    def get_success_url(self):
        messages.success(self.request,"Your Enquiry Deleted Successfully!")
        return reverse('dashboard:enquiry_come')

class  EnquirySendDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model=Enquiry
    def get_success_url(self):
        messages.success(self.request,"Your Enquiry Deleted Successfully!")

        return reverse('dashboard:enquiry_send')


# add to favorite
@login_required
def favourite(request,pk):
    property=get_object_or_404(SellProperty,pk=pk)
    if property.favourite.filter(id=request.user.id).exists():
        property.favourite.remove(request.user)
        messages.success(request,'Remove from your favourite list!')
    else:
        property.favourite.add(request.user)
        messages.success(request,'Added your favourite list')
    return redirect(property.get_absolute_url())

@login_required
def remove_favourite(request,pk):
    property=get_object_or_404(SellProperty,pk=pk)
    if property.favourite.filter(id=request.user.id).exists():
        property.favourite.remove(request.user)
        messages.success(request,'Remove from your favourite list!')
    return redirect('dashboard:favourite_list')

class FavouriteList(ListView,LoginRequiredMixin):
    model = SellProperty
    template_name = 'favourite_list.html'

    def get_queryset(self):
        queryset=SellProperty.objects.all()
        queryset=queryset.filter(favourite=self.request.user)
        return queryset


def MakeOfferProperty(request,pk,slug):
    property=get_object_or_404(SellProperty,pk=pk,slug=slug)

    if MakeOffer.objects.filter(property=property).exists():
        data = MakeOffer.objects.get(property=property)
        form = MakeOfferForm(request.POST or None, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Offer updated successfully!')
            return redirect('dashboard:myoffer')
    else:
        if request.method == "POST":
            form=MakeOfferForm(request.POST or None)
            if form.is_valid():
                discount=request.POST.get('discount')
                data=MakeOffer.objects.create(property=property,discount=discount)
                data.save()
                messages.success(request,'Make offer successfully!')
                return redirect('dashboard:myoffer')
        else:
            form=MakeOfferForm()
    context={
        'form':form,
        'object':property,
    }
    return render(request,'make_offer.html',context)




class OfferList(ListView):
    modol=MakeOffer
    template_name = 'offer_list.html'

    def get_queryset(self):
        queryset=MakeOffer.objects.all()
        queryset=queryset.filter(property__realator=self.request.user)
        return queryset

class OfferRemove(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    model=MakeOffer

    def get_success_url(self):
        messages.success(self.request,"Your Property Offer Remove Successfully!")
        return reverse('dashboard:myoffer')
