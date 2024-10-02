from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdminDashboard.as_view(),name='admin-dashboard'),
    path('products/product-brands/',views.AdminProductBrandView.as_view(),name='admin-product-brands'),
]
