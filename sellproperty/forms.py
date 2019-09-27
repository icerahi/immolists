from django import forms


from .models import Type, SellProperty, Enquiry, MakeOffer


class SellPropertyForm(forms.ModelForm):

    class Meta:
        model=SellProperty
        exclude=('realator','slug','saved')



    def __init__(self, *args, **kwargs):
        super(SellPropertyForm, self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class']='form-control'
        self.fields['category'].widget.attrs['class']='form-control'
        self.fields['type'].widget.attrs['class']='form-control'
        self.fields['full_description'].widget.attrs['class']='form-control'
        self.fields['key_features'].widget.attrs['class']='form-control'
        self.fields['min_price'].widget.attrs['class'] = 'form-control'
        self.fields['max_price'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['main_image'].widget.attrs['class'] = 'form-control'
        self.fields['image_2'].widget.attrs['class'] = 'form-control'
        self.fields['image_3'].widget.attrs['class'] = 'form-control'
        self.fields['video'].widget.attrs['video']='form-control video_link float-right'
        self.fields['video'].widget.attrs['class'] = 'form-control'
        self.fields['action'].widget.attrs['class']='form-control'
        self.fields['rent_per'].widget.attrs['class']='form-control'
        self.fields['location'].widget.attrs['class']='form-control'


class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        exclude=('property',)

    def __init__(self,*args,**kwargs):
        super(EnquiryForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['phone'].widget.attrs['class']='form-control'
        self.fields['message'].widget.attrs['class']='form-control'

        self.fields['name'].widget.attrs['placeholder']='Name'
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['phone'].widget.attrs['placeholder']='Phone'
        self.fields['message'].widget.attrs['placeholder']='Message'

class MakeOfferForm(forms.ModelForm):


    class Meta:
        model=MakeOffer
        fields=('discount',)

    def __init__(self,*args,**kwargs):
        super(MakeOfferForm, self).__init__(*args,**kwargs)
        self.fields['discount'].widget.attrs['class']='form-control'
        self.fields['discount'].widget.attrs['placeholder'] = 'example 10% '



