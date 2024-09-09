from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.UserProfileView.as_view(),name='user-profile'),
    path('orders/',views.UserCompletedOrders.as_view(),name='orders'),
    path('profile-details/',views.UserProfileDetail.as_view(),name='profile-details'),
    path('address/',views.UserAddress.as_view(),name='address'),
]
