from django import forms
from product_module.models import ProductBrand
from order_module.models import OrderBasket,OrderDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column

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


class OrderDetailAdminModelForm(forms.ModelForm):

    class Meta:
        model=OrderDetail
        fields=['product','count','final_price']
        # fields='__all__'
        # exclude=['order_basket']

    #way 2 for add class and style in codes
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('product', css_class='form-group col-md-3 mb-0 input'),
    #             Column('count', css_class='form-group col-md-3 mb-0 input'),
    #             Column('final_price', css_class='form-group col-md-3 mb-0 input'),
    #             css_class='form-row'
    #         )
    #     )

    # def __init__(self, *args, **kwargs):
    #     super(OrderDetailAdminModelForm, self).__init__(*args, **kwargs)

    #     #Custom classok
    #     self.fields['product'].widget.attrs['class'] = 'input'
    #     self.fields['count'].widget.attrs['class'] = 'input'
    #     self.fields['final_price'].widget.attrs['class'] = 'input'


#way 3
# class OrderDetailForm(forms.ModelForm):
#     class Meta:
#         model = OrderDetail
#         fields = ['product', 'quantity', 'price']
#         widgets = {
#             'product': forms.TextInput(attrs={'class': 'form-control'}),
#             'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

# from django.forms import inlineformset_factory

# OrderDetailInlineFormSet = inlineformset_factory(OrderBasket, OrderDetail, form=OrderDetailForm, extra=3, max_num=5)
