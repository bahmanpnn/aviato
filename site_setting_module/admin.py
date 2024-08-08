from django.contrib import admin
from .models import SiteSetting,FooterLinkItem


admin.site.register(SiteSetting)
admin.site.register(FooterLinkItem)