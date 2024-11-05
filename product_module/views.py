from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from user_profile_module.models import UserFavoriteProduct
from order_module.models import OrderBasket,OrderDetail
from utils.http_service import get_client_ip
from utils.convertors import grouped_list
from .models import ProductCategory,Product,ProductSorting,ProductVisit,ProductImages,ProductComment
from .forms import ProductSortingForm
from itertools import chain
from permissions import is_authenticated_permission


class ProductView(View):
    template_name = 'product_module/products.html'
    
    def get(self, request,category=None, *args, **kwargs):
        categories = ProductCategory.objects.filter(is_active=True, is_delete=False, parent_id=None)
        products = Product.objects.filter(is_active=True, is_delete=False)

        # Search functionality
        # todo: add pagination and sorting for search field to user can visit next pages of search items
        search_field = request.GET.get('search_field', '')
        if search_field:
            products = products.filter(Q(title__icontains=search_field) | Q(short_description__icontains=search_field))

        # Category filter
        # category = request.GET.get('category', '')
        if category is not None:
            products = products.filter(category__url_title=category)

        # Sorting filter
        sort_filter = request.GET.get('sort', '')
        if sort_filter:
            try:
                sorting_option = ProductSorting.objects.get(url_title=sort_filter)
                if sorting_option.url_title == 'most-expensive':
                    products = products.order_by('-price')
                elif sorting_option.url_title == 'cheapest':
                    products = products.order_by('price')
                elif sorting_option.url_title in ['kids', 'women', 'men']:
                    products = products.filter(sorting=sorting_option)
            except ProductSorting.DoesNotExist:
                pass  # If sorting option does not exist, do nothing

        # Pagination
        paginator = Paginator(products, 6)  # Show 2 products per page
        page_number = request.GET.get('page', 1)
        try:
            products_page = paginator.page(page_number)
        except PageNotAnInteger:
            products_page = paginator.page(1)  # If page is not an integer, deliver first page
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)  # If page is out of range, deliver last page

        try:
            sorting_options = ProductSorting.objects.all().order_by('url_title')  # Fetch all sorting options
        except:
            sorting_options = None

        context = {
            'products': products_page,
            'categories': categories,
            'sorting_options': sorting_options,
            'selected_category': category,
            'selected_sort': sort_filter,
            'paginator': paginator,
        }
        return render(request, self.template_name, context)


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
                        'confirm_button_text':'OK',
                        'product_id':product_id,
                        'action':'removing'
                    })
            else:    
                add_product_to_favorites=UserFavoriteProduct(user_id=request.user.id,product_id=target_product.id)
                add_product_to_favorites.save()

                return JsonResponse({
                        'status':'success',
                        'title':'alert',
                        'text':'product added successfully',
                        'icon':'success',
                        'confirm_button_text':'OK',
                        'product_id':product_id,
                        'action':'adding'
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
        product_images.insert(0,loaded_product)
        context['product_all_images']=product_images
        context['product_images']=grouped_list(product_images,6)

        # product comments
        comments=ProductComment.objects.filter(product_id=loaded_product.id,parent_id=None).order_by('-created_date').prefetch_related('productcomment_set')
        context['comments']=comments
        # context['comments_count']=ProductComment.objects.filter(product_id=loaded_product.id).count()
        

        # # related products
        # todo: add query other products that bought with this product
        
        # way 1
        # baskets=OrderBasket.objects.prefetch_related('order_detail__product').exclude(order_detail__product_id=loaded_product.id).filter(is_paid=True,order_detail__product_id=loaded_product.id)
        
        # baskets=OrderBasket.objects.filter(is_paid=True,order_detail__product_id=loaded_product.id).prefetch_related('order_detail__product').exclude(order_detail__product_id=loaded_product.id)
        # print(list(baskets))
        # products_related=[]
        # for basket in baskets:
        #     for item in basket.order_detail.all():
        #         if len(products_related)<=4 and item.product.id !=loaded_product.id:
        #             products_related.append(item.product)
        # print(products)

        # way 2
        # related_product=OrderDetail.objects.filter(order_basket__is_paid=True)
        # for p in related_product:
        #     print(p.product)

        # related_products=Product.objects.filter(orderdetail__order_basket__is_paid=True).exclude(id=loaded_product.id)
        # related_products=Product.objects.filter(Q(brand_id=loaded_product.brand_id)|Q(category__in=loaded_product.category.all())).exclude(id=loaded_product.id)[:4]
        # todo:add products that category of them is same that product object in product detail view(use again set+category__in?) 
        related_products=Product.objects.filter(Q(brand_id=loaded_product.brand_id)).exclude(id=loaded_product.id).all()[:4]
        baskets=OrderBasket.objects.prefetch_related('order_detail').filter(is_paid=True,order_detail__product_id=loaded_product.id)

        products_related=set()
        for basket in baskets:
            for item in basket.order_detail.all():
                if len(products_related)<=4 and item.product.id !=loaded_product.id:
                    products_related.add(item.product)

        # context['related_products']=set(chain(related_products,products_related))
        context['related_products']=products_related.union(related_products)

        return context


def add_product_comment(request):
    if request.user.is_authenticated:
        product_id=int(request.GET.get('product_id'))
        check_product=get_object_or_404(Product,id=product_id,is_active=True,is_delete=False)
        
        if check_product is not None:
            comment=request.GET.get('comment')
            new_comment=ProductComment(author_id=request.user.id,product_id=product_id,
                                    parent_id=request.GET.get('parent_id'),comment_text=comment)
            new_comment.save()
            
            comments=ProductComment.objects.filter(product_id=product_id,parent_id=None).order_by('-created_date').prefetch_related('productcomment_set')
            # comments_count=ProductComment.objects.filter(product_id=product_id).count()
            
            data=render_to_string('product_module/includes/product_comments.html',{
                'comments':comments,
            })

            return JsonResponse({
                    'status':'success',
                    'body':data
                })
            # return render(request,'product_module/includes/product_comments.html',{
            # 'comments':comments
            # })

        else:
            return JsonResponse({
                'status':'invalid-product-id'
            })

    return JsonResponse({
        'status':'not-authenticated',
        'title':'alert',
        'text':'if you want to comment must login first',
        'icon':'error',
        'confirm_button_text':'OK'
        })
        



