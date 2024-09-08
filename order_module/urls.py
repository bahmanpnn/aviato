from django.urls import path
from . import views

urlpatterns = [
    path('add-product-to-basket/',views.add_product_to_basket,name='add-product-to-basket'),
    path('basket/',views.UserOrderBasket.as_view(),name='order-basket'),
    path('remove_product_from_basket/<detail_id>/',views.remove_product_from_basket,name='remove-product-from-basket'),
    path('remove_product_from_basket_ajax/',views.remove_product_from_basket_ajax,name='remove-product-from-basket-ajax'),
]