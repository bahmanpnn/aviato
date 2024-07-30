from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields=['full_name','email','subject','message']

        widgets={
            'full_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }),
            'subject':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Subject'
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control',
                'rows':6,
                'id':'message',
                'placeholder':'Message'
            })
        }

        error_messages={
            'full_name':{
                'required':'please fill this field',
                'max_length':'this field cant accept more 300 characters!! '
            },
            'email':{
                'required':'please fill this field',
            },
            'subject':{
                'required':'please fill this field',
            },
            'message':{
                'required':'please fill this field',
            },
        }