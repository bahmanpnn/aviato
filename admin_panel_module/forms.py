from django import forms
from product_module.models import ProductBrand


class ProductBrandAdminForm(forms.Form):
    title=forms.CharField(max_length=127)
    is_active=forms.BooleanField(required=False)


# class ProductBrandAdminForm(forms.ModelForm):
#     class Meta:
#         model=ProductBrand
#         fields=('title','is_active')
