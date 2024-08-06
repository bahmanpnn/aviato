from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register-page'),
    path('email-acive-code/<str:email_active_code>/',views.EmailActiveCode.as_view(),name='email-active-code'),
    path('login/',views.LoginView.as_view(),name='login-page'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('forget-password/',views.ForgetPasswordView.as_view(),name='forget-password-page'),
    path('reset-password/<str:email_reset_password_code>/',views.ResetPasswordView.as_view(),name='reset-password-page'),

]
