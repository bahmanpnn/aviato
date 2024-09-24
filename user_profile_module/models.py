from django.db import models
from product_module.models import Product
from account_module.models import User

class UserFavoriteProduct(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return self.product