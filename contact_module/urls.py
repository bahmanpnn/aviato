from django.urls import path
from . import views

urlpatterns = [
    # path('',views.contact_us,name='contact-us'),
    path('',views.ContactUsView.as_view(),name='contact-us'),
]
