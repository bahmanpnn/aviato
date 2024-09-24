from django.contrib import admin
from .models import UserFavoriteProduct



class UserFavoriteProductAdmin(admin.ModelAdmin):
    list_display=['product','user']

admin.site.register(UserFavoriteProduct,UserFavoriteProductAdmin)

