from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DetailView, DeleteView,TemplateView

from properties.forms import PropertyForSellForm
from properties.models import PropertyForSell, Type


class PropertyListView(ListView):
    model=PropertyForSell
    context_object_name='property'
    template_name = 'sell_list.html'



class PropertyCreateView(CreateView,LoginRequiredMixin):
    model=PropertyForSell
    form_class = PropertyForSellForm
    success_url = reverse_lazy('property_list')
    template_name = 'sell.html'

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




#Test Templates
######################### Dashboard #############################
class CheckTemplate(TemplateView):
    template_name='dashboard_base.html'


class MyList(TemplateView):
    template_name = 'mylist.html'

class FavouriteList(TemplateView):
    template_name = 'favourite.html'

class OfferList(TemplateView):
    template_name = 'offer.html'

class PersonalInfo(TemplateView):
    template_name = 'personalinfo.html'

class PasswordChange(TemplateView):
    template_name = 'password_change.html'

class Sell(TemplateView):
    template_name = 'sell.html'

class Rent(TemplateView):
    template_name = 'rent.html'
class MakeOffer(TemplateView):
    template_name = 'make_offer.html'

##########################################################################

## Actual Template test


class Home(TemplateView):
    template_name ='site/home.html'

def Search(request):
    return render(request,'site/search.html')

class CommingSoon(TemplateView):
    template_name = 'site/comming_soon.html'

class AgentList(TemplateView):
    template_name = 'site/realator_list.html'

class AboutAgent(TemplateView):
    template_name = 'site/profile.html'

class PropertyList(TemplateView):
    template_name = 'site/sell_list.html'

class single(TemplateView):
    template_name = 'site/detail_view.html'
class faq(TemplateView):
    template_name = 'site/faq.html'

class register(TemplateView):
    template_name = 'site/register.html'
class login(TemplateView):
    template_name = 'site/logins.html'
class forget_password(TemplateView):
    template_name = 'site/forget_password.html'

class error(TemplateView):
    template_name = 'site/error.html'
class contact(TemplateView):
    template_name = 'site/contact.html'

