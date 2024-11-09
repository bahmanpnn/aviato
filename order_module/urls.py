from django.urls import path
from . import views

urlpatterns = [
    path('add-product-to-basket/',views.add_product_to_basket,name='add-product-to-basket'),
    path('basket/',views.UserOrderBasket.as_view(),name='order-basket'),
    path('checkout/',views.UserCheckOutBasket.as_view(),name='order-checkout'),
    path('remove_product_from_basket/<int:detail_id>/',views.remove_product_from_basket,name='remove-product-from-basket'),
    path('remove_basket_cart/<int:detail_id>/',views.remove_basket_cart,name="remove-basket-cart"),
    path('remove_product_from_basket_ajax/',views.remove_product_from_basket_ajax,name='remove-product-from-basket-ajax'),
    path('confirm_checkout/',views.confirm_checkout,name='confirm-checkout'),
]
