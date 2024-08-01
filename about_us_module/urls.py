from django.urls import path
from . import views

urlpatterns = [
    path('',views.AboutUsView.as_view(),name='about-us'),
    path('download_pdf/',views.download_shop_pdf,name='download-shop-pdf'),
    # path('pdf/',views.some_view,name='pdf-view'),
    # path('show_pdf/',views.ShowPDFView.as_view(),name='show-pdf-view'),
]
