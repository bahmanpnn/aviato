from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.template.loader import render_to_string
from django.contrib import messages
from product_module.models import Product
from .models import OrderBasket,OrderDetail
from permissions import is_authenticated_permission
import datetime
from .forms import CouponApplyForm
from .models import Coupon


def add_product_to_basket(request):
    if request.user.is_authenticated:
        
        product_id=int(request.GET.get('product_id'))
        count=int(request.GET.get('count')) #get method returns str
        if count<=0:
            return JsonResponse({
            'status':'not-invalid',
            'title':'alert',
            'text':'invalid count',
            'icon':'error',
            'confirm_button_text':'OK!!'
        })

        product=Product.objects.filter(id=product_id,is_active=True,is_delete=False).first()

        if product is not None:
            current_order,is_created=OrderBasket.objects.get_or_create(is_paid=False,user_id=request.user.id)
            current_order_detail=current_order.order_detail.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count+=count
                current_order_detail.save()
            else:
                new_order_detail=OrderDetail(product_id=product_id,count=count,order_basket_id=current_order.id)
                new_order_detail.save()
                
            return JsonResponse({
                'status':'success',
                'title':'alert',
                'text':'product added successfully',
                'icon':'success',
                'confirm_button_text':'OK'
            })
        else:
            return JsonResponse({
                'status':'not-invalid',
                'title':'alert',
                'text':'invalid count',
                'icon':'error',
                'confirm_button_text':'OK'
            })
    else:
        return JsonResponse({
            'status':'not-authenticated',
            'title':'alert',
            'text':'for adding product to basket you need to login first',
            'icon':'warning',
            'confirm_button_text':'return to login page'
        })


class UserOrderBasket(View,LoginRequiredMixin):
    template_name='order_module/basket.html'

    def get(self,request):
        current_basket,is_created=OrderBasket.objects.prefetch_related('order_detail').get_or_create(is_paid=False,user_id=request.user.id)

        return render(request,self.template_name,{
            'basket':current_basket,
            'total_price':current_basket.get_total_amount,
            })
    
    
class UserCheckOutBasket(View,LoginRequiredMixin):
    template_name='order_module/checkout.html'

    def dispatch(self, request, *args, **kwargs):
        self.current_basket,self.is_created=OrderBasket.objects.prefetch_related('order_detail').get_or_create(is_paid=False,user_id=request.user.id)
        return super().dispatch(request, *args, **kwargs)
    

    def get(self,request):
        # print(request.GET)

        if not self.is_created:
            return render(request,self.template_name,{
                'basket':self.current_basket,
                'total_price':self.current_basket.get_total_amount,
                })
        else:
            raise Http404() # remember it just raise in debug=False
        

@is_authenticated_permission
def remove_product_from_basket_ajax(request):
    detail_id=request.GET.get('detail_id')
    target_order_detail=OrderDetail.objects.filter(id=detail_id,order_basket__user_id=request.user.id,order_basket__is_paid=False).first()

    if target_order_detail is not None:
        target_order_detail.delete() 

    else:
        return JsonResponse({
            'status':'invalid-detail-id'
        })
    current_basket,is_created=OrderBasket.objects.prefetch_related('order_detail').get_or_create(is_paid=False,user_id=request.user.id)
    data=render_to_string('order_module/includes/basket_orders.html',{
        'basket':current_basket,
        'total_price':current_basket.get_total_amount
    })
    return JsonResponse({
            'status':'success',
            'body':data
        })


# todo:switch all redirects with next method to redirect user last page and url after actions!
@is_authenticated_permission
def remove_basket_cart(request,detail_id):
    if detail_id is not None:   
        target_order_detail=OrderDetail.objects.filter(id=detail_id,order_basket__user_id=request.user.id,order_basket__is_paid=False).first()
        if target_order_detail is not None:
            target_order_detail.delete()
            messages.success(request,'product removed successfully form your basket!!')
            return redirect(reverse('home-page'))
        else:
            messages.error(request,'product did not exist in your basket!!')
            redirect(reverse('home-page'))
    else:
        return redirect('home-page')


@is_authenticated_permission
def remove_product_from_basket(request,detail_id):
    if detail_id is not None:   
        target_order_detail=OrderDetail.objects.filter(id=detail_id).first()
        if target_order_detail is not None:
            target_order_detail.delete()
            messages.success(request,'product removed successfully form your basket!!')
            return redirect(reverse('order-basket'))
        else:
            messages.error(request,'product did not exist in your basket!!')
            redirect(reverse('order-basket'))
    else:
        return redirect('home-page')
      
      
def confirm_checkout(request):
    return render(request,'order_module/confirm_checkout.html')


class CouponApplyView(LoginRequiredMixin,View):
    form_class=CouponApplyForm

    def post(self,request):
        now=datetime.datetime.now()
        code=request.POST['code']
        try:
            coupon=Coupon.objects.get(code__exact=code,valid_from__lte=now,valid_to__gte=now,is_active=True)

        except Coupon.DoesNotExist:
            messages.error(request,'this coupon does not exists or maybe expired!!')
            return redirect('order-checkout')
            
        order=OrderBasket.objects.get(user_id=request.user.id,is_paid=False)
        order.discount=coupon.discount
        order.save()
        messages.success(request,'coupon added successfully')
        return redirect('order-checkout')
