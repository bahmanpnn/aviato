
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_module.urls')),
    path('contact_us/',include('contact_module.urls')),
]
