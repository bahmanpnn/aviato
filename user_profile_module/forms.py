from django import forms
from account_module.models import User,UserAddressInformation


class EditUserForm(forms.ModelForm):
    # user_image=forms.ImageField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','phone_number','about_user','image')


class ChangePasswordForm(forms.Form):
    last_password=forms.CharField(widget=forms.PasswordInput())
    new_password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    
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
