from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdminDashboard.as_view(),name='admin-dashboard'),
    # product-brands
    path('products/product-brands/',views.AdminProductBrandView.as_view(),name='admin-product-brands'),
    path('products/product-brands/delete/<int:brand_id>/',views.admin_product_brand_delete,name='admin-product-brands-delete'),
    path('products/product-brands/edit/<int:brand_id>/',views.EditProductBrandAdminView.as_view(),name='admin-product-brands-edit'),
    
    # accounts
    path('accounts/orders/',views.AccountOrderAdminView.as_view(),name='admin-account-orders'),
    path('accounts/orders/delete/<int:basket_id>/',views.admin_order_basket_delete,name='admin-order-basket-delete'),
    path('accounts/orders/edit/<int:basket_id>/',views.EditOrderBasketAdminView.as_view(),name='admin-order-basket-edit'),

    # product category

]
