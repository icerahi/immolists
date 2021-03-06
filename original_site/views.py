from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Max, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView

from accounts.models import Profile
from sellproperty.forms import EnquiryForm
from sellproperty.models import SellProperty, Enquiry, Category, MakeOffer


class Home(ListView):
    template_name = 'site/home.html'
    model = SellProperty

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        object_list = SellProperty.published.all()
        context['object_list'] = object_list
        context['categories']=Category.objects.all()
        return context

def PropertyDetail(request,pk,slug):

    property=get_object_or_404(SellProperty,pk=pk,slug=slug) # get single object
    viewed=request.session.get('viewed',[])  # view variable
    if viewed:
        if property.id not in viewed:
            viewed.append(property.id)
            request.session['viewed']=viewed
            property.views+=1
            property.save()
    else:
        viewed=[property.id]
        request.session['viewed']=viewed
        property.views+=1
        property.save()
    is_favourite=False
    if property.favourite.filter(id=request.user.id).exists():
        is_favourite=True

    if request.method=='POST':
        form=EnquiryForm(request.POST)
        if form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            data=Enquiry.objects.create(property=property,name=name,email=email,phone=phone,message=message)
            data.save()
            messages.success(request,'Your Enquiry message successfully send to Property Owner!')
            return HttpResponseRedirect(property.get_absolute_url())
        else:
            messages.warning(request,'Your Enquiry not send,please fill the form correctly!')
    else:
        if request.user.is_authenticated:
            form=EnquiryForm(initial={'name':request.user.realator.fullname,'email':request.user.email,
                                      'phone':request.user.realator.phone,
                                      'message':"""Hello,

Please contact me, I am interested in properties that you have listed on Immolists.

Best Regards. """})
        else:
            form=EnquiryForm()
    map_url='http://maps.googleapis.com/maps/api/staticmap?center=%(latitude)s,%(longitude)s&zoom=%(zoom)s&size=%(width)sx%(height)s&maptype=roadmap&markers=%(latitude)s,%(longitude)s&sensor=false&visual_refresh=true&scale=%(scale)s&key=%(key)s" width="%(width)s" height="%(height)s">' % {
                'latitude': property.location.latitude,
                'longitude': property.location.longitude,
                'key': getattr(settings, 'PLACES_MAPS_API_KEY'),
                'zoom': 15,
                'width': 100,
                'height': 100,
                'scale': 2
            }

    other_properties = SellProperty.published.all().filter(realator=property.realator).order_by('?')[:3]
    top_properties=SellProperty.published.all().order_by('-views')[:3]

    context={
        'form':form,
        'object':property,
        'is_favourite':is_favourite,
        'map_url':map_url,
        'other_properties':other_properties,
        'top_properties':top_properties,

    }

    return render(request,'site/detail_view.html',context)


class ProfileView(DetailView,LoginRequiredMixin):
    template_name='site/profile.html'
    queryset= User.objects.all()

    def get_object(self,queryset=None):
        return get_object_or_404(User,username__iexact=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context=super(ProfileView, self).get_context_data(**kwargs)
        context['sell_properties']=SellProperty.published.all().filter(action='sale',realator=self.get_object())
        context['rent_properties']=SellProperty.published.all().filter(action='rent',realator=self.get_object())
        return context

class RealatorList(ListView):
    template_name = 'site/realator_list.html'
    model =  Profile

class SellList(ListView):
    template_name = 'site/sell_list.html'
    model = SellProperty

    def get_queryset(self):
        queryset=SellProperty.published.all().filter(action='sale')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SellList, self).get_context_data(**kwargs)
        context['action'] = 'Sale'
        return context

class RentList(ListView):
    template_name = 'site/sell_list.html'
    model=SellProperty
    def get_queryset(self):
        queryset=SellProperty.published.all().filter(action='rent')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RentList, self).get_context_data(**kwargs)
        context['action'] = 'Rent'
        return context

class OfferForSell(ListView):
    template_name = 'site/offer_list.html'
    model=MakeOffer
    def get_queryset(self):
        queryset=MakeOffer.objects.all().filter(property__action='sale')
        return queryset
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(OfferForSell, self).get_context_data(**kwargs)
        context['offer_for']='Sale'
        return context

class OfferForRent(ListView):
    template_name = 'site/offer_list.html'
    model=MakeOffer
    def get_queryset(self):
        queryset=MakeOffer.objects.all().filter(property__action='rent')
        return queryset
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(OfferForRent, self).get_context_data(**kwargs)
        context['offer_for']='Rent'
        return context

#search
def Search(request):
    categories=Category.objects.all()
    status=request.GET.get('status')
    keywords=request.GET.get('keywords')
    category=request.GET.get('category')
    price=request.GET.get('price')

    if price is not None:
        min_price = price.split(';')[0]
        max_price = price.split(';')[1]


    if status or keywords or price :
        properties=SellProperty.published.filter(
            Q(action__icontains=status)|
            Q(category__name__icontains=category)|
            Q(max_price__icontains=max_price) |
            Q(min_price__icontains=min_price) |
            Q(min_price__range=(min_price,max_price)) |
            Q(max_price__range=(min_price,max_price)) |
            Q(realator__username__icontains=keywords)|
            Q(realator__realator__fullname__icontains=keywords)|
            Q(type__name__icontains=keywords)|
            Q(title__icontains=keywords)|
            Q(full_description__icontains=keywords)|
            Q(key_features__icontains=keywords)|
            Q(created__icontains=keywords)|
            Q(rent_per__icontains=keywords)|
            Q(location__icontains=keywords)|
            Q(realator__realator__about__icontains=keywords)

              )



    context={
        "categories":categories,
        'properties':properties,
    }
    return render(request,'site/search.html',context)

class Faq(TemplateView):
    template_name = 'site/faq.html'
class Privacy(TemplateView):
    template_name = 'site/privacy.html'
class Terms(TemplateView):
    template_name = 'site/terms.html'

class Contact(TemplateView):
    template_name = 'site/contact.html'

class BaseTest(TemplateView):
    template_name = 'site/base_test.html'
