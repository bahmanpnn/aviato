from django.shortcuts import render
from django.views import View


class ProductView(View):
    template_name='product_module/products.html'
    
    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        pass


class ProductDetailView(View):
    template_name='product_module/product_detail.html'
    
    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request):
        pass
