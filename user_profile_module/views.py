from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth import logout
from order_module.models import OrderBasket
from account_module.models import User,UserAddressInformation
from .forms import EditUserForm,EditUserAddressForm,ChangePasswordForm
from .models import UserFavoriteProduct


class UserProfileView(View):
    template_name='user_profile_module/dashboard.html'
    
    def get(self,request):
        user_orders=OrderBasket.objects.annotate(items=Count('order_detail')).filter(is_paid=True,user_id=request.user.id)
        return render(request,self.template_name,{
            'user_orders':user_orders
        })



class UserCompletedOrders(View):
    template_name='user_profile_module/orders.html'
    
    def get(self,request,basket_id):
        target_basket_details=OrderBasket.objects.prefetch_related('order_detail').filter(id=basket_id,is_paid=True,user_id=request.user.id).first()
        
        if target_basket_details is None:
            raise Http404('invalid order detail id!!')
        
        return render(request,self.template_name,{
            'target_basket_details':target_basket_details
        })

    
class UserProfileDetail(View):
    template_name='user_profile_module/profile_details.html'
    form_class = EditUserForm
    second_form_class=ChangePasswordForm

    def dispatch(self, request, *args, **kwargs):
        self.target_user=User.objects.get(id=request.user.id)
        return super().dispatch(request, *args, **kwargs)
    

    def get(self,request):
        return render(request,self.template_name,{
            'form': self.form_class(instance=request.user),
            'change_password_form':ChangePasswordForm(),
            'current_user':self.target_user
        })

    def post(self,request):
        
        change_password_form=self.second_form_class(request.POST)
        if change_password_form.is_valid():
            cd=change_password_form.cleaned_data
            check_last_password=self.target_user.check_password(cd['last_password'])
            if check_last_password:
                self.target_user.set_password(cd['new_password'])
                self.target_user.save()
                messages.success(request,'your password changed successfully')
                logout(request)
                return redirect(reverse('login-page'))

        form=self.form_class(request.POST,files=request.FILES,instance=self.target_user)
        if form.is_valid():
            form.save()
            messages.success(request,'your profile updated successfully')
        
        return render(request,self.template_name,{
            'form': form,
            'change_password_form':ChangePasswordForm(),
            'current_user':self.target_user
        })


class UserAddress(View):
    template_name='user_profile_module/address.html'
    form_class=EditUserAddressForm
    
    def dispatch(self, request, *args, **kwargs):
        self.user_addresses=UserAddressInformation.objects.filter(user_id=request.user.id)
        return super().dispatch(request, *args, **kwargs)
    

    def get(self,request):
        
        forms=[]
        for user_address in self.user_addresses:
            forms.append(self.form_class(instance=user_address))
        return render(request,self.template_name,{
            'user_addresses':self.user_addresses,
            'forms':forms,
            'new_address_form':EditUserAddressForm()
        })

    def post(self,request):

        print(request.POST)
        if 'id_address_counter' in request.POST:
            counter=int(request.POST['id_address_counter'])-1
            
            if counter<=len(self.user_addresses):
                target_address_form=self.user_addresses[counter]
                # print(target_address_form)
                
            form=self.form_class(request.POST,instance=target_address_form)
            if form.is_valid():
                form.save()
            messages.success(request,'your address updated successfully')    
        else:
            print(request.POST['id_add_new_address'])
            new_address_form=EditUserAddressForm(request.POST)
            if new_address_form.is_valid():
                cd=new_address_form.cleaned_data
                new_address=UserAddressInformation(address=cd['address'],user_id=request.user.id,receiver_full_name=cd['receiver_full_name'],country=cd['country'],phone=cd['phone'])
                new_address.save()
            messages.success(request,'new address added successfully')
                
        return redirect(reverse('address'))
    

def user_address_remove(request,user_address_id):
    target_user_address=get_object_or_404(UserAddressInformation,user_id=request.user.id,id=user_address_id)
    if target_user_address is not None:
        target_user_address.delete()
        messages.success(request,'address removed successfully')
        return redirect(reverse('address'))
    

def user_favorite_products(request):
    user_favorite_products=UserFavoriteProduct.objects.filter(user_id=request.user.id).order_by('product__added_date')

    return render(request,'user_profile_module/user_favorites.html',{
        'user_favorite_products':user_favorite_products
    })