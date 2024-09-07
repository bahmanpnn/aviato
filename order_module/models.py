from django.db import models
# from django.core.validators import MinValueValidator,MaxValueValidator
from account_module.models import User
from product_module.models import Product

class OrderBasket(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    is_paid=models.BooleanField(default=False)
    payment_date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return str(self.user)
    
    def get_total_amount(self):
        if self.is_paid:
            total_amount=0
            for order_detail in self.order_detail.all():
                total_amount+=order_detail.final_price *order_detail.count
        
        total_amount=0
        for order_detail in self.order_detail.all():
            total_amount+=order_detail.product.price *order_detail.count
        
        return total_amount
    

class OrderDetail(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    order_basket=models.ForeignKey(OrderBasket,on_delete=models.CASCADE,related_name='order_detail')
    count=models.PositiveIntegerField()
    final_price=models.BigIntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.order_basket)
    
    def get_total_price(self):
        return self.product.price * self.count
    


# class Coupon(models.Model):
#     code=models.CharField(max_length=15,unique=True)
#     valid_from=models.DateTimeField()
#     valid_to=models.DateTimeField()
#     discount=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(90)])
#     is_active=models.BooleanField(default=False)

#     def __str__(self):
#         return self.code