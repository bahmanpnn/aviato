from django.contrib import admin
from .models import Product,ProductBrand,ProductCategory,\
                            ProductSorting,ProductVisit,ProductImages,ProductComment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'is_active', 'added_date')
    search_fields = ('title', 'short_description')
    list_filter = ('is_active', 'category', 'sorting')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('url_title', 'is_active', 'is_delete')
    search_fields = ('title',)


class ProductSortingAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title', 'is_active', 'is_delete')
    search_fields = ('title', 'url_title')


class ProductImagesAdmin(admin.ModelAdmin):
    list_display=['product_id','product']

admin.site.register(ProductImages,ProductImagesAdmin)
admin.site.register(ProductVisit)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(ProductSorting,ProductSortingAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductComment)

