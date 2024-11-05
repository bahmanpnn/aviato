import requests
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.utils.crypto import get_random_string
from site_setting_module.models import SiteSetting
from utils.email_service import email_service
from .forms import LoginViewForm,registerform,ForgetPasswordForm,ResetPasswordForm
from .models import User


class RegisterView(View):
    template_name="account_module/register.html"
    form_class=registerform

    def get(self,request):
        return render(request,self.template_name,{
            'form':self.form_class()
        })

    def post(self,request):

        form=self.form_class(request.POST)

        if form.is_valid():
            cd=form.cleaned_data
            new_user=User(username=cd['username'],email=cd['email'],is_active=False,email_active_code=get_random_string(63))
            new_user.set_password(cd['password'])
            new_user.save()

            # send email
            site_setting=SiteSetting.objects.filter(is_main_setting=True).first()
            email_template='account_module/email/register_email.html'
            email_service('activing account',new_user.email,{'user':new_user,'site_setting':site_setting},email_template)

            messages.success(request,'your account created successfully! now check your email to active your account')
            return redirect('home-page')
        
        return render(request,self.template_name,{
            'form':form
        })       


class EmailActiveCode(View):
    def get(self,request,email_active_code):
        # check_user:User=User.objects.filter(email_active_code__iexact=email_active_code).first() ***
        check_user=User.objects.filter(email_active_code__iexact=email_active_code).first()
        
        #todo:add time for email active code or ban ip if try more to active account or banned(is_ban=True?) before
        # if check_user and not check_user.is_active and check_user.is_ban =='False' :
        
        # if check_user is not None and not check_user.is_active:
        if check_user is not None:
            print(check_user)
            check_user.is_active=True
            check_user.save()
            messages.success(request,'your account actived!! now you can login')
            return redirect('login-page')

        messages.warning(request,'your email active code is expired or wrong!!')
        return redirect('home-page')


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

            check_user_email=User.objects.filter(email__iexact=cd['email_or_phone_number']).first()
            check_user_phone_number=User.objects.filter(phone_number__iexact=cd['email_or_phone_number']).first()
            if check_user_email:
                if check_user_email.check_password(cd['password']) and check_user_email.is_active:
                    login(request,check_user_email,backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request,'you logged in successfully')
                    return redirect('home-page')
            
            elif check_user_phone_number:
                if check_user_phone_number.check_password(cd['password']) and check_user_phone_number.is_active:
                    login(request,check_user_phone_number,backend='django.contrib.auth.backends.ModelBackend')
                    messages.success(request,'you logged in successfully')
                    return redirect('home-page')
            
            # else:
            #     messages.warning(request,'your username or password is wrong!! try again please')

                
        
        messages.warning(request,'your username/phone number or password is wrong!! try again please')
        return render(request,self.template_name,{
            'form':form
        })


class LogoutView(View,LoginRequiredMixin):
    def get(self,request):
        logout(request)
        messages.success(request,'you logged out successfully',extra_tags='success')

        response = redirect('home-page')
        response.delete_cookie('sessionid')

        try:
            requests.get('https://github.com/logout')
        except:
            pass
        
        return response


class ForgetPasswordView(View):
    template_name="account_module/forget_password.html"
    from_class=ForgetPasswordForm

    def get(self,request):
        return render(request,self.template_name,{
            'form':self.from_class()
        })

    def post(self,request):
        form=self.from_class(request.POST)

        if form.is_valid():
            check_email=User.objects.filter(email__iexact=form.cleaned_data['email']).exists()


            if check_email:
                # send email
                target_user=User.objects.get(email__iexact=form.cleaned_data['email'])
                site_setting=SiteSetting.objects.filter(is_main_setting=True).first()
                email_template='account_module/email/reset_password_email.html'
                email_service('reset password',form.cleaned_data['email'],{'user':target_user,'site_setting':site_setting},email_template)

                messages.success(request,'email sent successfully!! check your messages to reset your password')
                return redirect(reverse('login-page'))
            else:
                form.add_error('email','this email does not exists in our site!!')

        return render(request,self.template_name,{
            'form':form
        })


class ResetPasswordView(View):
    template_name='account_module/reset_password.html'
    form_class=ResetPasswordForm

    def get(self,request,email_reset_password_code):
        # check_code=get_object_or_404(User,email_active_code__iexact=email_reset_password_code)
        # check_code=User.objects.get(email_active_code__iexact=email_reset_password_code)
        
        # if not check_code:
        #     messages.warning(request,'this code is expired or not exists!')
        #     return redirect(reverse('login-page'))
        
        check_code=User.objects.filter(email_active_code__iexact=email_reset_password_code).first()
        
        if check_code is None:
            messages.warning(request,'this code is expired or not exists!')
            # return redirect(reverse('login-page'))
            raise Http404()
        
        return render(request,self.template_name,{
            'form':self.form_class()
        })
    
    def post(self,request,email_reset_password_code):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=User.objects.get(email_active_code__iexact=email_reset_password_code)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'your password changed successfully!! now you can login :))')
            return redirect(reverse('login-page'))
        
        return render(request,self.template_name,{
            'form':form
        })
    


# class LoginView(View):
#     template_name="account_module/login.html"
#     form_class=LoginViewForm

#     def get(self,request):
#         return render(request,self.template_name,{
#             'form':self.form_class()
#         })

#     def post(self,request):
#         form=self.form_class(request.POST)

#         if form.is_valid():
#             cd=form.cleaned_data

#             check_phone_number=User.objects.filter(phone_number=cd['email_or_phone_number']).exists()
#             if check_phone_number:
#                 user=authenticate(request,phone_number=cd['email_or_phone_number'],password=cd['password'])
#                 if user is not None:
#                     login(request,user)
#                     messages.success(request,'you logged in successfully!!',extra_tags='success')
#                     return redirect('home-page')

#             check_email=User.objects.filter(email=cd['email_or_phone_number']).exists()
#             if check_email:
#                 check_user=User.objects.get(email=cd['email_or_phone_number'])
#                 check_user_password=check_user.check_password(cd['password'])
                
#                 if check_user_password:
#                     login(request,check_user)
#                     messages.success(request,'you logged in successfully!!',extra_tags='success')
#                     return redirect('home-page')
#                 else:
#                     messages.error(request,'password or email-phone_number is wrong!! ',extra_tags='danger')
#             else:
#                 messages.error(request,'password or email-phone_number is wrong!! ',extra_tags='danger')
        
#         return render(request,self.template_name,{
#             'form':form
#         })



