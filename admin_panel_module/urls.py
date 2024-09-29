from django.urls import path
from . import views

urlpatterns = [
    path('',views.AdminDashboard.as_view(),name='admin-dashboard'),
]
