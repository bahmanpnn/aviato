from django.shortcuts import render


def index(request):
    return render(request,'home_module/index.html')

def navbar_component(request):
    return render(request,'navbar_component.html')

def header_component(request):
    return render(request,'header_component.html')

def slider_component(request):
    return render(request,'home_module/slider_component.html')

def footer_component(request):
    return render(request,'footer_component.html')