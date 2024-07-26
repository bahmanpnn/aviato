from django.shortcuts import render


def contact_us(request):
    return render(request,'contact_module/contact_us.html')