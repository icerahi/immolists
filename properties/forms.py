from django import forms


from .models import PropertyForSell,Type

class PropertyForSellForm(forms.ModelForm):


    class Meta:
        model=PropertyForSell
        exclude=('realator','slug','saved')

    def __init__(self, *args, **kwargs):
        super(PropertyForSellForm, self).__init__(*args,**kwargs)
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
        self.fields['image'].widget.attrs['class']='form-control'




