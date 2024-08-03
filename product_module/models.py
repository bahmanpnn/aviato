from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

class ProductBrand(models.Model):
    title=models.CharField(max_length=300,db_index=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title    

    class Meta:
        verbose_name='brand'
        verbose_name_plural='brands'


class ProductCategory(models.Model):
    title=models.CharField(max_length=300,db_index=True)
    url_title=models.CharField(max_length=300)
    is_active=models.BooleanField(default=True)
    is_delete=models.BooleanField(default=False)

    def __str__(self):
        return self.url_title
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'


class Product(models.Model):
    title=models.CharField(max_length=300,db_index=True)
    price=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)
    is_delete=models.BooleanField(default=False)
    added_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(db_index=True)
    content=models.TextField()
    short_description=models.CharField(max_length=320,db_index=True)
    brand=models.ForeignKey(ProductBrand,on_delete=models.SET_NULL,blank=True,null=True)
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,blank=True)
    rating=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(1)],blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("product-detail", args=[self.slug])
        # return reverse("product-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'
    
    def __str__(self):
        return self.title
    

