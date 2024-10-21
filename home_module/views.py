from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.db.models import Sum,Count
from site_setting_module.models import SiteSetting,FooterLinkItem
from product_module.models import Product
from product_module.models import ProductCategory
from .models import Slider,UserEmailSubscribe
from .forms import GetUserEmailForSubscribeForm,SearchForm


def index(request):
    form=GetUserEmailForSubscribeForm()

    if request.method=="POST":
        form=GetUserEmailForSubscribeForm(request.POST)
        if form.is_valid():
            new_email=UserEmailSubscribe(email=form.cleaned_data.get('email'))
            new_email.save()
            messages.success(request,'thank you for sending your email to fallowing us')
            return redirect(reverse('home-page'))
        
    product_category_banner_right=ProductCategory.objects.filter(is_delete=False,is_banner=True,position__exact=ProductCategory.ProductCategoryPosition.right).first()
    product_category_banner_top_left=ProductCategory.objects.filter(is_delete=False,is_banner=True,position__exact=ProductCategory.ProductCategoryPosition.top_left).first()
    product_category_banner_bottom_left=ProductCategory.objects.filter(is_delete=False,is_banner=True,position__exact=ProductCategory.ProductCategoryPosition.bottom_left).first()
   
    most_viewed_products=Product.objects.filter(is_active=True,is_delete=False).annotate(visit_count=Count('productvisit')).order_by('-visit_count')[:6]
    trend_products=Product.objects.annotate(buy_count=Sum('orderdetail__count')).filter(is_active=True,is_delete=False,orderdetail__order_basket__is_paid=True).order_by('-buy_count')[:9]
    
    return render(request,'home_module/index.html',{
        'form':form,
        'trend_products':trend_products,
        'product_category_banner_right':product_category_banner_right,
        'product_category_banner_top_left':product_category_banner_top_left,
        'product_category_banner_bottom_left':product_category_banner_bottom_left,
        'most_viewed_products':most_viewed_products
    })


def navbar_component(request):
    return render(request,'navbar_component.html')

def header_component(request):
    site_settings=SiteSetting.objects.filter(is_main_setting=True).first()

    return render(request,'header_component.html',{
        'site_settings':site_settings,
        'search_form':SearchForm()
    })

def slider_component(request):
    sliders=Slider.objects.filter(is_active=True)
    
    return render(request,'home_module/slider_component.html',{
        'sliders':sliders
    })

def footer_component(request):
    footer_link_items=FooterLinkItem.objects.all()
    site_settings=SiteSetting.objects.filter(is_main_setting=True).first()
    
    return render(request,'footer_component.html',{
        'footer_link_items':footer_link_items,
        'site_settings':site_settings
    })


