from django import forms


class GetUserEmailForSubscribeForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter Your Email Address'
    }))

class SearchForm(forms.Form):
    search_field=forms.CharField(max_length=255,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Search...'
    }))