from django.urls import path
from . import views

urlpatterns = [
    path('',views.AboutUsView.as_view(),name='about-us'),
    path('resume/',views.resume_view,name='resume'),
    
]
