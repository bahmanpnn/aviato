from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView
from django.http import JsonResponse,HttpResponse
from utils.http_service import get_client_ip
from user_profile_module.models import UserFavoriteProduct
from order_module.models import OrderBasket,OrderDetail
from utils.convertors import grouped_list
from .models import ProductCategory,Product,ProductSorting,ProductVisit,ProductImages
from .forms import ProductSortingForm


class ProductView(View):
    template_name='product_module/products.html'
    form_class=ProductSortingForm
    
    def get(self,request,*args,**kwargs):
        categories=ProductCategory.objects.filter(is_active=True,is_delete=False,parent_id=None)
        products=Product.objects.filter(is_active=True,is_delete=False).order_by('-added_date')
        
        sorting=request.GET.get('sorting')
        if sorting is not None:
            products.filter(sorting__url_title__iexact=sorting) 
            print(products)  
        
        category=kwargs.get('category')
        if category is not None:
            products=products.filter(category__url_title__iexact=category,is_active=True)
    
    
        return render(request,self.template_name,{
            'categories':categories,
            'products':products,
            'form':self.form_class()
        })
    
    def post(self,request):
        pass


def add_remove_product_to_favorite_list(request):
    if request.user.is_authenticated:
        product_id=int(request.GET.get('product_id'))
        target_product=get_object_or_404(Product,id=product_id,is_active=True,is_delete=False)
        if target_product is not None:
            check_product=UserFavoriteProduct.objects.filter(product_id=product_id,user_id=request.user.id).first()
            if check_product is not None:
                check_product.delete()
                return JsonResponse({
                        'status':'success',
                        'title':'alert',
                        'text':'product removed successfully',
                        'icon':'success',
                        'confirm_button_text':'OK'
                    })
            else:    
                add_product_to_favorites=UserFavoriteProduct(user_id=request.user.id,product_id=target_product.id)
                add_product_to_favorites.save()

                return JsonResponse({
                        'status':'success',
                        'title':'alert',
                        'text':'product added successfully',
                        'icon':'success',
                        'confirm_button_text':'OK'
                    })
        
        else:
            return JsonResponse({
                'status':'invalid-product-id',
                'title':'alert',
                'text':'invalid product id',
                'icon':'error',
                'confirm_button_text':'OK'
            })
    else:
        return JsonResponse({
            'status':'not-authenticated',
            'title':'alert',
            'text':'if you want to add this product to your favorite,first must login or register',
            'icon':'error',
            'confirm_button_text':'OK'
            })
    

def add_one_product_to_basket(request):
    if request.user.is_authenticated:
        product_id=int(request.GET.get('product_id'))
        count=1
        target_product=get_object_or_404(Product,id=product_id,is_active=True,is_delete=False)

        if target_product is not None:
            current_order,is_created=OrderBasket.objects.get_or_create(is_paid=False,user_id=request.user.id)
            current_order_detail=current_order.order_detail.filter(product_id=product_id).first()

            if current_order_detail is not None:
                current_order_detail.count+=count
                current_order_detail.save()
            else:
                new_order_detail=OrderDetail(product_id=product_id,count=count,order_basket_id=current_order.id)
                new_order_detail.save()


            return JsonResponse({
                    'status':'success',
                    'title':'alert',
                    'text':'product added to basket successfully',
                    'icon':'success',
                    'confirm_button_text':'OK'
                })
        
        else:
            return JsonResponse({
                'status':'invalid-product-id',
                'title':'alert',
                'text':'invalid product id',
                'icon':'error',
                'confirm_button_text':'OK'
            })
    else:
        return JsonResponse({
            'status':'not-authenticated',
            'title':'alert',
            'text':'if you want to add this product to your favorite,first must login or register',
            'icon':'error',
            'confirm_button_text':'OK'
            })
    

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
        user_ip=get_client_ip(self.request)        
        has_been_visited=ProductVisit.objects.filter(ip__exact=user_ip,product_id=loaded_product.id).exists()

        if self.request.user.is_authenticated:
            user_id=self.request.user.id
        else:
            user_id=None
        if not has_been_visited:
            new_visit=ProductVisit(ip=user_ip,product_id=loaded_product.id,user_id=user_id)
            new_visit.save()

        product_images=list(ProductImages.objects.filter(product_id=loaded_product.id).all())
        print(product_images)
        product_images.insert(0,loaded_product)
        context['product_all_images']=product_images
        context['product_images']=grouped_list(product_images,6)


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
