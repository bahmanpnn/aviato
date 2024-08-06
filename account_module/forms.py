from django import forms
from .models import User
from django.core.exceptions import ValidationError


class registerform(forms.Form):
    
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }),
    error_messages={
        'required':'this field is required'
    })

    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'
    }),
    error_messages={
        'required':'this field is required'
    })

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }),
    error_messages={
        'required':'this field is required'
    })

    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm Password'
    }),
    error_messages={
        'required':'this field is required'
    })

    def clean_email(self):
        email=self.cleaned_data.get('email')
        check_email=User.objects.filter(email__iexact=email)
        if check_email:
            raise ValidationError('this email used before please use another one')
        
        return email
    
    # todo:combine clean_username+clean_email
    def clean_username(self):
        username=self.cleaned_data.get('username')
        check_username=User.objects.filter(username__iexact=username)
        if check_username:
            raise ValidationError('this username used before please use another one')
        
        return username
    
    def clean_confirm_password(self):
        password=self.cleaned_data.get('password')
        confirm_password=self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('password and confirm password does not match')
        
        return confirm_password
        

class LoginViewForm(forms.Form):

    email_or_phone_number=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control text-center',
        'placeholder':'Email or Phone Number'
    }))

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control text-center',
        'placeholder':'Password'
    }))

    # todo:check ip that dont try more than 5 times that fill password wrong in every 6 hours
    def clean_email_or_phone_number(self): 
        '''
            this uses in validation list of login form and check username exists or not
        '''
        email_or_phone_number=self.cleaned_data.get('email_or_phone_number')
        check_email=User.objects.filter(email__iexact=email_or_phone_number).exists()
        if check_email:
            return email_or_phone_number
        else:
            check_phone_number=User.objects.filter(phone_number__iexact=email_or_phone_number).exists()
            if check_phone_number:
                return email_or_phone_number
            else:
                raise ValidationError('your password or username is wrong!! try again please')


# class LoginViewForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

        widgets={
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password'
            })
        }


class ForgetPasswordForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control text-center',
        'placeholder':'Enter Your Email'
    }),
    error_messages={
        'required':'this field is required'
    })

    # def clean_email(self):
    #     email=self.cleaned_data.get('email')
    #     check_email=User.objects.filter(email__iexact=email).exists()
        
    #     if check_email:
    #         return email
        
    #     else:
    #         return ValidationError('this email does not exists!!')





