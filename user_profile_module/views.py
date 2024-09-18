from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.db.models import Count
from order_module.models import OrderBasket
from .forms import EditUserForm,EditUserAddressForm
from account_module.models import User,UserAddressInformation
from django.contrib import messages


class UserProfileView(View):
    template_name='user_profile_module/dashboard.html'
    
    def get(self,request):
        user_orders=OrderBasket.objects.annotate(items=Count('order_detail')).filter(is_paid=True,user_id=request.user.id)
        return render(request,self.template_name,{
            'user_orders':user_orders
        })

    def post(self,request):
        pass


class UserCompletedOrders(View):
    template_name='user_profile_module/orders.html'
    
    def get(self,request,order_id):
        target_basket_details=OrderBasket.objects.prefetch_related('order_detail').filter(is_paid=True,user_id=request.user.id).first()
        if target_basket_details is None:
            raise Http404('invalid order detail id!!')
        return render(request,self.template_name,{
            'target_basket_details':target_basket_details
        })

    
class UserProfileDetail(View):
    template_name='user_profile_module/profile_details.html'
    form_class = EditUserForm

    def dispatch(self, request, *args, **kwargs):
        self.target_user=User.objects.get(id=request.user.id)
        return super().dispatch(request, *args, **kwargs)
    

    def get(self,request):
        return render(request,self.template_name,{
            'form': self.form_class(instance=request.user),
            'current_user':self.target_user
        })

    def post(self,request):
        form=self.form_class(request.POST,files=request.FILES,instance=self.target_user)

        if form.is_valid():
            form.save()

        messages.success(request,'your profile updated successfully')    
        return render(request,self.template_name,{
            'form': form,
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
            'forms':forms
        })

    def post(self,request):
        counter=int(request.POST['id_address_counter'])-1
        
        if counter<=len(self.user_addresses):
            target_address_form=self.user_addresses[counter]
            # print(target_address_form)
            
        form=self.form_class(request.POST,instance=target_address_form)
        if form.is_valid():
            form.save()
        
        forms=[]
        for user_address in self.user_addresses:
            forms.append(self.form_class(instance=user_address))

        messages.success(request,'your address updated successfully')    
        return render(request,self.template_name,{
            'user_addresses':self.user_addresses,
            'forms':forms
        })
    

def user_address_remove(request,user_address_id):
    target_user_address=get_object_or_404(UserAddressInformation,user_id=request.user.id,id=user_address_id)
    if target_user_address is not None:
        target_user_address.delete()
        messages.success(request,'address removed successfully')
        return redirect(reverse('address'))