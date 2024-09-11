from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.db.models import Count
from order_module.models import OrderBasket


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
    
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass


class UserAddress(View):
    template_name='user_profile_module/address.html'
    
    def get(self,request):
        return render(request,self.template_name)

    def post(self,request):
        pass