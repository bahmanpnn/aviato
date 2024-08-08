from django.shortcuts import render
from django.views import View
from .models import Slider
from site_setting_module.models import SiteSetting,FooterLinkItem

def index(request):
    return render(request,'home_module/index.html')

def navbar_component(request):
    return render(request,'navbar_component.html')

def header_component(request):
    site_settings=SiteSetting.objects.filter(is_main_setting=True).first()

    return render(request,'header_component.html',{
        'site_settings':site_settings
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


