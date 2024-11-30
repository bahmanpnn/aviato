from django import forms
from .models import ContactUs
from django.utils.translation import gettext_lazy as _


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields=['full_name','email','subject','message']

        widgets={
            'full_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':_('Your Name')
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':_('Your Email')
            }),
            'subject':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':_('Subject')
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control',
                'rows':6,
                'id':'message',
                'placeholder':_('Message')
            })
        }

        message=_('please fill this field')
        error_messages={
            'full_name':{
                'required':message,
                'max_length':_('this field cant accept more 300 characters!! ')
            },
            'email':{
                'required':message,
            },
            'subject':{
                'required':message,
            },
            'message':{
                'required':message,
            },
        }