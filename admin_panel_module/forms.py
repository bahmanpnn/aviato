from django import forms
from product_module.models import ProductBrand,Product,ProductExtraImage
from order_module.models import OrderBasket,OrderDetail
from django.forms import inlineformset_factory
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Row, Column


class ProductAdminModelForm(forms.ModelForm):
    #     # Note: Do NOT define FormSet as a class attribute
    #     # Create an inline formset
    #     ProductImageFormSet = inlineformset_factory(
    #         Product,  # Parent model
    #         ProductExtraImage,  # Child model
    #         fields=['image'],  # Fields to include in the formset
    #         extra=3,  # Number of empty forms to display
    #         max_num=5,  # Maximum number of forms
    #         )
    class Meta:
        model = Product
        fields = ['title', 'is_active', 'is_delete', 'price', 'image', 'brand', 'category']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control input-sm',
                'placeholder': 'product title',
                'style': 'width:150px;'
            })
        }

    # def __init__(self, *args, **kwargs):
    #     # Create the formset in the __init__ method
    #     super().__init__(*args, **kwargs)
        
    #     # Create the inline formset
    #     self.image_formset = inlineformset_factory(
    #         Product,  # Parent model
    #         ProductExtraImage,  # Child model
    #         fields=['image'],  # Fields to include in the formset
    #         extra=3,  # Number of empty forms to display
    #         max_num=5,  # Maximum number of forms
    #         can_delete=True  # Allow deletion of existing images
    #     )
        
    #     # If this is an existing product, pass the instance to the formset
    #     if self.instance.pk:
    #         self.images_formset = self.image_formset(
    #             instance=self.instance,
    #             queryset=ProductExtraImage.objects.filter(product=self.instance)
    #         )
    #     else:
    #         # For a new product, create an empty formset
    #         self.images_formset = self.image_formset()

    # def is_valid(self):
    #     # Override is_valid to validate both the main form and the formset
    #     main_form_valid = super().is_valid()
        
    #     # Validate the formset
    #     images_formset_valid = self.images_formset.is_valid()
        
    #     return main_form_valid and images_formset_valid

    # def save(self, commit=True):
    #     # Save the main product form
    #     instance = super().save(commit=commit)
        
    #     # Save the formset with the product instance
    #     if commit:
    #         # Associate formset with the product instance
    #         self.images_formset.instance = instance
            
    #         # Save the formset
    #         self.images_formset.save()
        
    #     return instance


class ProductExtraImageForm(forms.ModelForm):
    class Meta:
        model = ProductExtraImage
        fields = ['image']

ImageFormSet = inlineformset_factory(Product, ProductExtraImage, form=ProductExtraImageForm,extra=0)

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
                # 'required':False
            })
            }


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

# way2 
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
