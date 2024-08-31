from django.urls import path
from . import views

urlpatterns = [
    path('',views.ProductView.as_view(),name='products'),
    path('product-category/<str:category>/',views.ProductView.as_view(),name='products-by-category'),
    path('<slug:slug>/',views.ProductDetailView.as_view(),name='product-detail'),
]
