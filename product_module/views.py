from django.shortcuts import render
from django.views import View
from .models import ProductCategory,Product


class ProductView(View):
    template_name='product_module/products.html'
    
    def get(self,request):
        categories=ProductCategory.objects.filter(is_active=True,is_delete=False,parent_id=None)
        products=Product.objects.filter(is_active=True,is_delete=False).order_by('-added_date')
        
        return render(request,self.template_name,{
            'categories':categories,
            'products':products
        })
    
    def post(self,request):
        pass


class ProductDetailView(View):
    template_name='product_module/product_detail.html'
    
    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        pass
