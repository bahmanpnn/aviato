from django.db import models
# from django.core.validators import MinValueValidator,MaxValueValidator
from account_module.models import User
from product_module.models import Product
from django.core.validators import MinValueValidator,MaxValueValidator


class OrderBasket(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    is_paid=models.BooleanField(default=False)
    payment_date=models.DateTimeField(null=True,blank=True)
    discount=models.PositiveIntegerField(null=True,blank=True,default=None)

    def __str__(self):
        return str(self.user)
    
    def get_total_price(self):
        total= sum(item.get_cost() for item in self.order_items.all())
        if self.discount:
            discount_price=(self.discount / 100 )*total
            return int(total-discount_price)
        return total
    
    def get_total_amount(self):
        if self.is_paid:
            total_amount=0
            if self.discount:
                for order_detail in self.order_detail.all():
                    total_amount+=order_detail.final_price *order_detail.count
                discount_price=(self.discount / 100 )*total_amount
                return float(total_amount-discount_price)
            
            for order_detail in self.order_detail.all():
                total_amount+=order_detail.final_price *order_detail.count
        else:
            total_amount=0
            if self.discount:
                for order_detail in self.order_detail.all():
                    total_amount+=order_detail.product.price *order_detail.count
                discount_price=(self.discount / 100 )*total_amount
                return float(total_amount-discount_price)
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
    

class OrderSubmittedAddress(models.Model):
    order_basket=models.ForeignKey(OrderBasket,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    fullname=models.CharField(max_length=127)
    address=models.CharField(max_length=127)
    zip_code=models.CharField(max_length=127)
    city=models.CharField(max_length=127)
    country=models.CharField(max_length=127)


class Coupon(models.Model):
    code=models.CharField(max_length=15,unique=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()
    discount=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(99)])
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.code