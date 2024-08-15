from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from site_setting_module.models import SiteSetting,FooterLinkItem
from .models import Slider,UserEmailSubscribe
from .forms import GetUserEmailForSubscribeForm
from django.contrib import messages

def index(request):
    form=GetUserEmailForSubscribeForm()

    if request.method=="POST":
        form=GetUserEmailForSubscribeForm(request.POST)
        if form.is_valid():
            new_email=UserEmailSubscribe(email=form.cleaned_data.get('email'))
            new_email.save()
            messages.success(request,'thank you for sending your email to fallowing us')
            return redirect(reverse('home-page'))
        
    return render(request,'home_module/index.html',{
        'form':form
    })

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


