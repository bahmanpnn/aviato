from django import forms
from django.utils.translation import gettext_lazy as _


class GetUserEmailForSubscribeForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':_('Enter Your Email Address')
    }))

class SearchForm(forms.Form):
    search_field=forms.CharField(max_length=255,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':_('Search...')
    }))