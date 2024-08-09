from django.urls import path
from . import views

urlpatterns = [
    path('',views.AboutUsView.as_view(),name='about-us'),
    # path('pdf/',views.some_view,name='pdf-view'),
]
