from django import forms


class UserEmailSubscribeForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Email Address'
    }))