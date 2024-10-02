from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdminDashboard.as_view(),name='admin-dashboard'),
    # product-brands
    path('products/product-brands/',views.AdminProductBrandView.as_view(),name='admin-product-brands'),
    path('products/product-brands/delete/<int:brand_id>/',views.admin_product_brand_delete,name='admin-product-brands-delete'),
    path('products/product-brands/edit/<int:brand_id>/',views.admin_product_brand_edit,name='admin-product-brands-edit'),

    # product category
]
