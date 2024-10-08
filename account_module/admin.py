from django.contrib import admin
from .models import User,UserAddressInformation

class UserInfoAdmin(admin.ModelAdmin):
    list_display=['username','is_superuser','phone_number','email']

admin.site.register(User,UserInfoAdmin)

class UserAddressInfoAdmin(admin.ModelAdmin):
    list_display=['user','receiver_full_name','phone']
    list_filter=['user','receiver_full_name']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.receiver_full_name=request.user.get_full_name()
        return super().save_model(request, obj, form, change)
    

admin.site.register(UserAddressInformation,UserAddressInfoAdmin)
