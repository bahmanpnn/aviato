from django.urls import path
from . import views


urlpatterns = [
    path('send-request/',views.send_request,name='send-request'),
    path('verify-payment/',views.verify_payment,name='verify-payment'),
]