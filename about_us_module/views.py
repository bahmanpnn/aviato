from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.conf import settings
from site_setting_module.models import SiteSetting
import os
import base64

class AboutUsView(View):
    template_name='about_us_module/about_us.html'
    
    def get(self,request):
        site_settings=SiteSetting.objects.filter(is_main_setting=True).first()

        return render(request,self.template_name,{
            'site_settings':site_settings
        })


def resume_view(request):
    pdf_path = os.path.join(settings.STATICFILES_DIRS[0], 'resume.pdf')
    with open(pdf_path, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read()).decode('utf-8')
    return render(request, 'about_us_module/resume.html', {'resume':encoded_string}) 


def video_view(request):
    return render(request, 'about_us_module/video.html')

