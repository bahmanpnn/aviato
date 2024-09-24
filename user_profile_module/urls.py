from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.UserProfileView.as_view(),name='user-profile'),
    path('orders/<int:order_id>/',views.UserCompletedOrders.as_view(),name='order-list'),
    path('profile-details/',views.UserProfileDetail.as_view(),name='profile-details'),
    path('address/',views.UserAddress.as_view(),name='address'),
    path('address-remove/<int:user_address_id>',views.user_address_remove,name='address-remove'),
    path('my-favorites/',views.user_favorite_products,name='user-favorite-products'),
]
