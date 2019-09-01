from django import forms
from django.contrib.auth.models import User
from address.forms import AddressField,AddressWidget

from .models import Profile

class UserEditForm(forms.ModelForm):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={
        "class":"form-control",
    }))


    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={
        'class':'form-control',

    }))
    class Meta:
        model=User
        fields=('username','email')




class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'type': 'date'
    }))



    class Meta:
        model=Profile
        exclude=('realator',)

        field_classes = {
            'address': AddressField,
        }
        widgets = {
            'address': AddressWidget,
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args,**kwargs)
        self.fields['fullname'].widget.attrs['class']='form-control'
        self.fields['image'].widget.attrs['class']='form-control'
        self.fields['about'].widget.attrs['class']='form-control'
        self.fields['phone'].widget.attrs['class']='form-control'
        self.fields['date_of_birth'].widget.attrs['class']='form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'





