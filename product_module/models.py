from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
from django.utils.text import slugify
from account_module.models import User

class ProductBrand(models.Model):
    title=models.CharField(max_length=300,db_index=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.title    

    class Meta:
        verbose_name='brand'
        verbose_name_plural='brands'


class ProductCategory(models.Model):
    class ProductCategoryPosition(models.TextChoices):
        right='right','position of this banner is enitre of right'
        top_left='top_left','position of this banner is top of left side'
        bottom_left='bottom_left','position of this banner is bottom of left side'

    parent=models.ForeignKey('ProductCategory',on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=300,db_index=True)
    url_title=models.CharField(max_length=300)
    is_active=models.BooleanField(default=True)
    is_delete=models.BooleanField(default=False)
    is_banner=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/product-category-banners',blank=True,null=True)
    position=models.CharField(max_length=150,choices=ProductCategoryPosition.choices,blank=True,null=True)
    short_description_banner=models.CharField(max_length=511,null=True,blank=True)
    

    def __str__(self):
        return self.url_title
    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'


class ProductSorting(models.Model):
    parent=models.CharField(max_length=127,default='all')
    title=models.CharField(max_length=300,db_index=True)
    url_title=models.CharField(max_length=300)
    is_active=models.BooleanField(default=True)
    is_delete=models.BooleanField(default=False)

    def __str__(self):
        return self.url_title
    
    class Meta:
        verbose_name='sorting'
        verbose_name_plural='sortings'


class ProductImages(models.Model):
    image=models.ImageField(upload_to='images/product-extra-images')
    product=models.ForeignKey('Product',on_delete=models.CASCADE)


class Product(models.Model):

    image=models.ImageField(upload_to='images/products',null=True,blank=True)
    title=models.CharField(max_length=300,db_index=True)
    price=models.PositiveIntegerField()
    discount_price=models.PositiveIntegerField(null=True,blank=True)
    is_active=models.BooleanField(default=True)
    is_delete=models.BooleanField(default=False)
    added_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True,null=True,db_index=True)
    content=models.TextField(null=True,blank=True)
    short_description=models.CharField(max_length=320,db_index=True,null=True,blank=True)
    brand=models.ForeignKey(ProductBrand,on_delete=models.SET_NULL,blank=True,null=True)
    category=models.ManyToManyField(ProductCategory)
    rating=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)],blank=True,null=True)
    sorting=models.ForeignKey(ProductSorting,on_delete=models.PROTECT,null=True,blank=True)
    
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
    

class ProductVisit(models.Model):
    ip=models.CharField(max_length=32)
    user=models.ForeignKey(User,on_delete=models.PROTECT,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product} - {self.ip}'
    