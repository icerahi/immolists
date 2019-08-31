from django import forms


from .models import  Type, SellProperty


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
        self.fields['location'].widget.attrs['class'] = 'form-control'
        self.fields['google_map'].widget.attrs['class'] = 'form-control'
        self.fields['main_image'].widget.attrs['class'] = 'form-control'
        self.fields['image_2'].widget.attrs['class'] = 'form-control'
        self.fields['image_3'].widget.attrs['class'] = 'form-control'





