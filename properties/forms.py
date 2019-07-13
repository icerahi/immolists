from django import forms
from pagedown.widgets import PagedownWidget

from .models import PropertyForSell,Type

class PropertyForSellForm(forms.ModelForm):
    full_description=forms.CharField(widget=PagedownWidget())
    key_features=forms.CharField(widget=PagedownWidget())
    class Meta:
        model=PropertyForSell
        fields = '__all__'


    def __init__(self,*args,**kwargs):
        super(PropertyForSellForm, self).__init__(*args,**kwargs)
        self.fields['type'].queryset=Type.objects.none()

        if 'category' in self.data:
            try:
                category_id=int(self.data.get('country'))
                self.fields['type'].queryset=Type.objects.filter(category_id=category_id).order_by('name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.field['type'].queryset=self.instance.category.type_set.order_by('name')

