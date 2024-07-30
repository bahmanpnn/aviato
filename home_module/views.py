from django.shortcuts import render
from django.views import View
from .models import Slider

def index(request):
    return render(request,'home_module/index.html')

def navbar_component(request):
    return render(request,'navbar_component.html')

def header_component(request):
    return render(request,'header_component.html')

def slider_component(request):
    sliders=Slider.objects.filter(is_active=True)
    
    return render(request,'home_module/slider_component.html',{
        'sliders':sliders
    })

def footer_component(request):
    return render(request,'footer_component.html')


# about us
class AboutUsView(View):
    template_name='home_module/about_us.html'
    def get(self,request):
        return render(request,self.template_name)