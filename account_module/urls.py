from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login-page'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('sign-in/',views.SignInView.as_view(),name='sign-in-page'),
    path('forget-password/',views.ForgetPasswordView.as_view(),name='forget-password-page'),
]
