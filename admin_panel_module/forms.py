from django import forms
from product_module.models import ProductBrand
from order_module.models import OrderBasket,OrderDetail


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

"""
    date = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    To apply this on a forms.ModelForm:

    class MyModelForm(forms.ModelForm):
        class Meta:
            model = MyModel
            fields = ['my_field', 'date']
            widgets = {
                'date': forms.widgets.DateInput(attrs={'type': 'date'})
            }
"""

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class DateInput(forms.DateInput):
    input_type = 'date'


class BasketAdminModelForm(forms.ModelForm):
    class Meta:
        model=OrderBasket
        fields=['user','is_paid','payment_date']
        widgets = {
            'payment_date': DateTimeInput()
        }

        # widgets={
        #     'title':forms.TextInput(attrs={
        #         'class':'form-control input-sm',
        #         'placeholder':'brand title',
        #         'required':False
        #     })
        #     }
