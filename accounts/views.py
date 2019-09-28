from django.contrib import messages

from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DetailView

from accounts.forms import ProfileForm
from accounts.models import Profile


class PersonalInformation(DetailView,LoginRequiredMixin):
    queryset = User.objects.all()
    template_name = 'personalinfo.html'

    def get_object(self, queryset=None):
        return get_object_or_404(User,username__iexact=self.kwargs.get('username'))


@login_required()
def profile_edit(request,username):
    username=request.user.username
    if request.method=="POST":
        profile_form=ProfileForm(request.POST or None,request.FILES,instance=request.user.realator)
        from allauth.account.forms import UserForm
        user_form  =UserEditForm(request.POST or None,instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.realator=request.user
            user_form.user=request.user
            user_form.email=request.user.email
            profile_form.save(commit=True)
            user_form.save(commit=True)
            messages.success(request,'Your Profile Information Update Successfully!')
            return redirect('dashboard:personal_info',username=request.user.username)
        else:
            messages.warning(request, 'Please fill the form with correct information!')
    else:
        profile_form=ProfileForm(instance=request.user.realator)
        user_form=UserEditForm(instance=request.user)

    context={
            'user_form':user_form,
            'profile_form':profile_form,
        }
    return render(request,'profile_edit.html',context)

