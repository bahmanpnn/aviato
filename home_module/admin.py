from django.contrib import admin
from .models import Slider,UserEmailSubscribe
from ckeditor.widgets import CKEditorWidget
from django import forms


class SliderAdminForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'
        widgets = {
            'text': CKEditorWidget(),  # Use CKEditor for the content field
        }


class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm

    class Media:
        js = ('home_module/js/ckeditor_inject.js',)  # Include your custom JavaScript


admin.site.register(Slider,SliderAdmin)
admin.site.register(UserEmailSubscribe)