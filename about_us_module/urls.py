from django.urls import path
from . import views

urlpatterns = [
    path('',views.AboutUsView.as_view(),name='about-us'),
    
    #way4 
    # path('pdf/',views.pdf_view,name='pdf-view'),
    # path('show_pdf/',views.show_pdf_view,name='show-pdf-view'),
]
