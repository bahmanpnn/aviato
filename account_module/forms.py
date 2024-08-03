from django import forms
from .models import User
from django.core.exceptions import ValidationError


class LoginViewForm(forms.Form):

    email_or_phone_number=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Email or Phone Number'
    }))

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))

    # def clean_email_or_phone_number(self): 
    #     '''
    #         this uses in validation list of login form and check username exists or not
    #     '''

    #     email_or_phone_number=self.cleaned_data['email_or_phone_number']
    #     if not User.objects.filter(email=email_or_phone_number).exists() or User.objects.filter(phone_number=email_or_phone_number).exists():
    #     # if not User.objects.filter(phone_number=email_or_phone_number).exists():
    #         raise ValidationError('try again please')
    #     return email_or_phone_number


# class LoginViewForm(forms.ModelForm):
    # class Meta:
    #     model=User
    #     fields=['username','password']

    #     widgets={
    #         'username':forms.TextInput(attrs={
    #             'class':'form-control',
    #             'placeholder':'Username'
    #         }),
    #         'password':forms.PasswordInput(attrs={
    #             'class':'form-control',
    #             'placeholder':'Password'
    #         })
    #     }