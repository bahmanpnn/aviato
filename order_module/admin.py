from django.contrib import admin
from .models import OrderBasket,OrderDetail,OrderSubmittedAddress


class OrderDetailInline(admin.TabularInline):
    model=OrderDetail
    raw_id_fields=('product',)
    # raw_id_fields=('product','order_basket')


@admin.register(OrderBasket)
class OrderAdmin(admin.ModelAdmin):
    '''
        this is main admin page that use OrderModel and 
        after data of Order model we can see Order Item model like table and
        default has 3 item in table that every item is one order item
    '''
    list_display=('id','user','payment_date','is_paid')
    list_filter=('is_paid',)
    inlines=(OrderDetailInline,) 


admin.site.register(OrderSubmittedAddress)