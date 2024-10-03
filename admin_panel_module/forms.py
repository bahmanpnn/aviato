from django import forms
from product_module.models import ProductBrand


class ProductBrandAdminForm(forms.Form):
    title=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control input-sm',
        'placeholder':'brand title'
    }),max_length=127,required=False)
    is_active=forms.BooleanField(required=False)


class ProductBrandAdminModelForm(forms.ModelForm):
    class Meta:
        model=ProductBrand
        fields=('title','is_active')

        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control input-sm',
                'placeholder':'brand title',
                'required':False
            })
            }
