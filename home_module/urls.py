from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home-page'),
    path('about-us/',views.AboutUsView.as_view(),name='about-us'),
]
