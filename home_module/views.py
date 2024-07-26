from django.shortcuts import render


def index(request):
    return render(request,'home_module/index.html')