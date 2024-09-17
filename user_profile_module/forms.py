from django import forms
from account_module.models import User


class EditUserForm(forms.ModelForm):
    # user_image=forms.ImageField()

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','phone_number','about_user','image')


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
