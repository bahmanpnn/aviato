from django.contrib import admin
from .models import Product,ProductBrand,ProductCategory,ProductSorting,ProductVisit,ProductImages


admin.site.register(Product)

class ProductImagesAdmin(admin.ModelAdmin):
    list_display=['product_id','product']

admin.site.register(ProductImages,ProductImagesAdmin)
admin.site.register(ProductVisit)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ProductSorting)