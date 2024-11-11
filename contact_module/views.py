from django.shortcuts import redirect, render
from django.views import View
from .forms import ContactUsModelForm
from django.contrib import messages
from site_setting_module.models import SiteSetting


class ContactUsView(View):
    try:
        site_settings=SiteSetting.objects.filter(is_main_setting=True).first()
    except:
        site_settings=None
        
    def get(self,request):

        return render(request,'contact_module/contact_us.html',{
            'form':ContactUsModelForm(),
            'site_settings':self.site_settings
        })
    
    def post(self,request):
        form=ContactUsModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your message send successfully')
            return redirect('contact-us')
        
        return render(request,'contact_module/contact_us.html',{
            'form':form,
            'site_settings':self.site_settings
        })


def test_map(request):
    return render(request,'contact_module/test_map.html')


def faq_view(request):
    return render(request,'contact_module/faq.html')