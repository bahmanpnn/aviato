from django.contrib import admin
from .models import Product,ProductBrand,ProductCategory,ProductSorting,ProductVisit


admin.site.register(Product)
admin.site.register(ProductVisit)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)
admin.site.register(ProductSorting)