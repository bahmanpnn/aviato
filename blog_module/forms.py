from django import forms
from django.utils.translation import gettext_lazy as _


class UserEmailSubscribeForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':_('Enter Your Email Address')
    }))