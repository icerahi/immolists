from django import forms


from .models import PropertyForSell,Type

class PropertyForSellForm(forms.ModelForm):


    class Meta:
        model=PropertyForSell
        exclude=('realator','slug','saved')
    def __int__(self):
        super(PropertyForSellForm, self).__int__(*args,**kwargs)
        self.fields['category'].widget.attrs['class']='category'



