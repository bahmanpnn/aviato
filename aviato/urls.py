from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('set_language/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
    path('admin-panel/',include('admin_panel_module.urls')),
    path('zibal/', include('zibal_gateway_module.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
]

urlpatterns += i18n_patterns(
    path('',include('home_module.urls')),
    path('contact-us/',include('contact_module.urls')),
    path('products/',include('product_module.urls')),
    path('about_us/',include('about_us_module.urls')),
    path('accounts/',include('account_module.urls')),
    path('blog/',include('blog_module.urls')),
    path('orders/',include('order_module.urls')),
    path('user/',include('user_profile_module.urls')),
    path('rosetta/', include('rosetta.urls')),
    prefix_default_language=True
    # if it is False it doesn't display default language in url==> # website.com/en/==>website.com
)

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
