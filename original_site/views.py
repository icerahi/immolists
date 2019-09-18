from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from accounts.models import Profile
from sellproperty.forms import EnquiryForm
from sellproperty.models import SellProperty, Enquiry, Category


class Home(ListView):
    template_name = 'site/home.html'
    model = SellProperty

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        object_list = SellProperty.published.all()
        context['object_list'] = object_list
        context['categories']=Category.objects.all()
        return context

def PropertyDetailView(request,pk,slug):

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
        form=EnquiryForm(request.POST or None)
        if form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            message=request.POST.get('message')
            data=Enquiry.objects.create(property=property,name=name,email=email,phone=phone,message=message)
            data.save()
            return HttpResponseRedirect(property.get_absolute_url())
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

    other_properties = SellProperty.objects.all().filter(realator=property.realator).order_by('?')[:3]
    top_properties=SellProperty.objects.all().order_by('-views')[:3]

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
        context['sell_properties']=SellProperty.objects.all().filter(action='sale',realator=self.get_object())
        context['rent_properties']=SellProperty.objects.all().filter(action='rent',realator=self.get_object())
        return context

class RealatorList(ListView):
    template_name = 'site/realator_list.html'
    model =  Profile

class SellList(ListView):
    template_name = 'site/sell_list.html'
    model = SellProperty