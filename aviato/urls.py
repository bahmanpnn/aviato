from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_module.urls')),
    path('contact-us/',include('contact_module.urls')),
    path('products/',include('product_module.urls')),
    path('about_us/',include('about_us_module.urls')),
    path('accounts/',include('account_module.urls')),
    path('blog/',include('blog_module.urls')),
    path('orders/',include('order_module.urls')),
    path('user/',include('user_profile_module.urls')),
    path('admin-panel/',include('admin_panel_module.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('zibal/', include('zibal_gateway_module.urls')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
