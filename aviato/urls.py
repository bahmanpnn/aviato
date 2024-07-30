
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_module.urls')),
    path('contact-us/',include('contact_module.urls')),
    path('products/',include('product_module.urls')),
]
