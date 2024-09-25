from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductView.as_view(),name='products'),
    path('add-to-user-favorite-list/',views.add_remove_product_to_favorite_list,name='add-product-to-favorite-list'),
    path('add-one-to-basket/',views.add_one_product_to_basket,name='add-one-product-to-basket'),
    path('product-category/<str:category>/',views.ProductView.as_view(),name='products-by-category'),
    path('<slug:slug>/',views.ProductDetailView.as_view(),name='product-detail'),
]
