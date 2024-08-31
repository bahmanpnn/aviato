from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView
from .models import ProductCategory,Product


class ProductView(View):
    template_name='product_module/products.html'
    
    def get(self,request,*args, **kwargs):
        categories=ProductCategory.objects.filter(is_active=True,is_delete=False,parent_id=None)
        products=Product.objects.filter(is_active=True,is_delete=False).order_by('-added_date')
        
        category=kwargs.get('category')
        if category is not None:
            products=products.filter(category__url_title__iexact=category,is_active=True)
        

        return render(request,self.template_name,{
            'categories':categories,
            'products':products
        })
    
    def post(self,request):
        pass


class ProductDetailView(DetailView):
    template_name='product_module/product_detail.html'
    model=Product

    def get_queryset(self):
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        loaded_product=self.object

        context['categories']=ProductCategory.objects.filter(product=loaded_product)
        
        # product visit adding and get user ip
        # user_ip=get_client_ip(self.request)
        # if self.request.user.is_authenticated:
        #     user_id=self.request.user.id
        # else:
        #     user_id=None
        
        # has_been_visited=ProductVisit.objects.filter(ip__exact=user_ip,product_id=loaded_product.id).exists()
        # if not has_been_visited:
        #     new_visit=ProductVisit(ip=user_ip,product_id=loaded_product.id,user_id=user_id)
        #     new_visit.save()

        # product_images=list(ProductImages.objects.filter(product_id=loaded_product.id).all())
        # product_images.insert(0,loaded_product)
        # context['product_images']=grouped_list(product_images,3)


        # # related products
        # related_products=list(Product.objects.filter(brand_id=loaded_product.brand_id).exclude(id=loaded_product.id).all()[:12])
        # context['related_products']=grouped_list(related_products,3)

        return context



# class ProductDetailView(View):
#     template_name='product_module/product_detail.html'
    
#     def get(self,request,*args, **kwargs):
#     def get(self,request,slug):
#         product=get_object_or_404(Product,slug=kwargs['slug'],is_active=True,is_delete=False)
#         return render(request,self.template_name,{
#             'product':product
#         })
    
#     def post(self,request):
#         pass
