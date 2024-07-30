from django.shortcuts import redirect, render
from django.views import View
from .forms import ContactUsModelForm
from django.contrib import messages


def contact_us(request):

    if request.method == 'POST':
        form=ContactUsModelForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,'your message send successfully',extra_tags='success')
            return redirect('contact-us')
        else:
            return render(request,'contact_module/contact_us.html',{
                'form':form
            })

    return render(request,'contact_module/contact_us.html',{
        'form':ContactUsModelForm()
    })

class ContactUsView(View):
    def post(self,request):
        form=ContactUsModelForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request,'your message send successfully',extra_tags='success')
            return redirect('contact-us')
        else:
            return render(request,'contact_module/contact_us.html',{
                'form':form
            })
        
    def get(self,request):
        return render(request,'contact_module/contact_us.html',{
            'form':ContactUsModelForm()
        })