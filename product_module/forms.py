from django import forms
from .models import ProductSorting


'''

# iterable 
CHOICES =( 
    ("1", "One"), 
    ("2", "Two"), 
    ("3", "Three"), 
    ("4", "Four"), 
    ("5", "Five"), 
) 


'''


class ProductSortingForm(forms.Form):

    product_sortings_list=[]
    for item in ProductSorting.objects.filter(is_active=True,is_delete=False):
        product_sortings_list.append((item.url_title,item))

    sorting=forms.ChoiceField(label='',choices=product_sortings_list,widget=forms.Select(attrs={
        'onchange': 'submit();',
        'class':'form-control text-capitalize',
        # 'style':'text-transform: capitalize;'
        }))
    


# $('#search_field').change(function(){
#     $('#your_form').submit()
# });