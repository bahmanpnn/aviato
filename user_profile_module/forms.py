from django import forms
from account_module.models import User,UserAddressInformation
from django.utils.translation import gettext_lazy as _


class EditUserForm(forms.ModelForm):
    # user_image=forms.ImageField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','phone_number','about_user','image')
        labels = {
            "username":_("username"),
            "first_name":_("first name"),
            "last_name":_("last name"),
            "email":_("email"),
            "phone_number":_("phone number"),
            "about_user":_("about user"),
            "image":_("image"),
        }


class ChangePasswordForm(forms.Form):
    last_password=forms.CharField(widget=forms.PasswordInput(),label=_("last password"))
    new_password=forms.CharField(widget=forms.PasswordInput(),label=_("new password"))
    confirm_password=forms.CharField(widget=forms.PasswordInput(),label=_("confirm password"))
    
    def clean_confirm_password(self):

        new_password=self.cleaned_data.get('new_password')
        confirm_password=self.cleaned_data.get('confirm_password')

        if new_password==confirm_password:
            return new_password
        
        raise forms.ValidationError('password does not match with confirm password please try again')
        # return ValidationError('confirm_password','password does not match with confirm password please try again')
        

class EditUserAddressForm(forms.ModelForm):
    class Meta:
        model=UserAddressInformation
        # fields='__all__'
        exclude=['user']
        labels={
            "address":_("address"),
            "receiver_full_name":_("receiver_full_name"),
            "country":_("country"),
            "phone":_("phone")
        }









# class AddPostForm(forms.ModelForm):
#     # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     # body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
#     # if we dont mark them they load first and before crispy using
#     class Meta:
#         model = Post
#         # fields = ['title', 'body'] ->it does not matter with [] or ()
#         fields = ('title', 'body')

# If you are using uni_form template pack,
# don’t forget to add the class ‘uniForm’ to your form(atrrs-->class).
