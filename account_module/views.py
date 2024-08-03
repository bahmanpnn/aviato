from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.contrib import messages
from .forms import LoginViewForm
from .models import User


class LoginView(View):
    template_name="account_module/login.html"
    form_class=LoginViewForm

    def get(self,request):
        return render(request,self.template_name,{
            'form':self.form_class()
        })

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            cd=form.cleaned_data

            check_phone_number=User.objects.filter(phone_number=cd['email_or_phone_number']).exists()
            if check_phone_number:
                user=authenticate(request,phone_number=cd['email_or_phone_number'],password=cd['password'])
                if user is not None:
                    login(request,user)
                    messages.success(request,'you logged in successfully!!',extra_tags='success')
                    return redirect('home-page')

            check_email=User.objects.filter(email=cd['email_or_phone_number']).exists()
            if check_email:
                check_user=User.objects.get(email=cd['email_or_phone_number'])
                check_user_password=check_user.check_password(cd['password'])
                
                if check_user_password:
                    login(request,check_user)
                    messages.success(request,'you logged in successfully!!',extra_tags='success')
                    return redirect('home-page')
                else:
                    messages.error(request,'password or email-phone_number is wrong!! ',extra_tags='danger')
            else:
                messages.error(request,'password or email-phone_number is wrong!! ',extra_tags='danger')
        
        return render(request,self.template_name,{
            'form':form
        })
                    


class LogoutView(View,LoginRequiredMixin):
    def get(self,request):
        logout(request)
        messages.success(request,'you logged out successfully',extra_tags='success')
        return redirect(reverse('home-page'))

class SignInView(View):
    template_name="account_module/sign_in.html"
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass


class ForgetPasswordView(View):
    template_name="account_module/forget_password.html"
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass