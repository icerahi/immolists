from django import forms
from .models import PropertyForSell,Type

class PropertyForSellForm(forms.ModelForm):

    class Meta:
        model=PropertyForSell
        fields = ['realator', 'category', 'type', 'title',]


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

