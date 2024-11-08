from django.contrib import admin
from .models import Product,ProductBrand,ProductCategory,\
                            ProductSorting,ProductVisit,ProductComment,ProductExtraImage
from admin_panel_module.forms import ProductAdminModelForm

# class ProductExtraImageInline(admin.TabularInline):
#     model = ProductExtraImage
#     extra = 3
#     max_num = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'is_active', 'added_date')
    search_fields = ('title', 'short_description')
    list_filter = ('is_active', 'category', 'sorting')

    # form = ProductAdminModelForm
    # inlines = [ProductExtraImageInline]
    
    # def get_form(self, request, obj=None, **kwargs):
    #     # Ensure the form is using our custom form
    #     kwargs['form'] = ProductAdminModelForm
    #     return super().get_form(request, obj, **kwargs)

    # def save_form(self, request, form, change):
    #     """
    #     Given a ModelForm return an unsaved instance. ``change`` is True if
    #     the object is being changed, and False if it's being added.
    #     """
    #     return form.save(commit=False)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('url_title', 'is_active', 'is_delete')
    search_fields = ('title',)


class ProductSortingAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title', 'is_active', 'is_delete')
    search_fields = ('title', 'url_title')
    

admin.site.register(ProductVisit)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(ProductSorting,ProductSortingAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductComment)

