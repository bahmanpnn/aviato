from django.urls import path
from . import views

urlpatterns = [
    path('',views.AboutUsView.as_view(),name='about-us'),
    path('resume/',views.resume_view,name='resume'),
    path('video/', views.video_view, name='video'),
]
