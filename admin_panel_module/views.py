from datetime import datetime,timedelta
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import ListView,DetailView
from django.db.models import Count,Sum
from django.contrib import messages
from product_module.models import ProductComment,Product,ProductBrand
from blog_module.models import ArticleComment
from order_module.models import OrderBasket
from account_module.models import User
from .forms import ProductBrandAdminForm,ProductBrandAdminModelForm


class AdminDashboard(View):
    template_name="admin_panel_module/dashboard.html"

    
    def get(self,request):
        # todo: use chain method to combine product and article comments to show in one scheduel
        latest_product_comments=ProductComment.objects.order_by('-created_date')[:6]
        latest_article_comments=ArticleComment.objects.order_by('-created_date')[:6]
        latest_sales=OrderBasket.objects.filter(is_paid=True).order_by('-payment_date')[:10]

        #statics
        """     
            https://www.geeksforgeeks.org/how-can-we-filter-a-date-of-a-datetimefield-in-django/
            start_date = date(2024, 1, 1)
            end_date = date(2024, 1, 31)
            events_in_range = Event.objects.filter(event_date__date__range=(start_date, end_date))
            #----
            start_datetime = datetime(2024, 1, 1)
            end_datetime = datetime(2024, 1, 31, 23, 59, 59)
            # Filtering by date range
            events_in_datetime_range = Event.objects.filter(
                event_date__gte=start_datetime,
                event_date__lte=end_datetime
            )
            #----
        
            https://gist.github.com/diptangsu/7c679e1785e2d5d8203693a7d64a47c9
            now = datetime.now()
            today_min = datetime.combine(now,  time.min)
            today_max = datetime.combine(now, time.max)
            objects = MyModel.objects.filter( Q(date__gte = today_min) & Q(date__lte = today_max) )
        """
        
        today=datetime.today()
        today_min = datetime.combine(timezone.now().date(), datetime.today().time().min)
        today_max = datetime.combine(timezone.now().date(), datetime.today().time().max)
        start_of_this_week_date =today - timedelta(days=int(datetime.weekday(datetime.now())))
        end_of_last_week_date =today - timedelta(days=int(datetime.weekday(datetime.now()))+1)
        start_of_last_week_date =today - timedelta(days=int(datetime.weekday(datetime.now()))+7)
        new_products = Product.objects.filter(added_date__range=(today_min, today_max)).count()
        new_users = int(User.objects.filter(date_joined__range=(today_min, today_max)).count())
        new_sales = OrderBasket.objects.filter(is_paid=True,payment_date__range=(today_min, today_max)).count()
        new_invoices = OrderBasket.objects.filter(is_paid=True,payment_date__range=(today_min, today_max))
        all_users=int(User.objects.filter(is_staff=False,is_superuser=False).count())
        growth_user=all_users/(all_users-new_users)*100 if new_users!=0 else 0
        new_users_percent=(new_users/all_users)*100 if all_users!=0 else 0
        last_users=new_users_percent-100 if new_users_percent is not 0 else 100
        this_week_sales=OrderBasket.objects.filter(is_paid=True,payment_date__gte=(start_of_this_week_date))
        last_week_sales=OrderBasket.objects.filter(is_paid=True,payment_date__range=(start_of_last_week_date, end_of_last_week_date))

        sales_total_amount=0
        for sale in new_invoices:
            sales_total_amount+=sale.get_total_amount()


        this_week_sales_amount=0
        for sale in this_week_sales:
            this_week_sales_amount+=sale.get_total_amount()

        print(this_week_sales_amount)

        last_week_sales_amount=0
        for sale in last_week_sales:
            last_week_sales_amount+=sale.get_total_amount()
        print(last_week_sales_amount)



        return render(request,self.template_name,{
            'product_comments':latest_product_comments,
            'article_comments':latest_article_comments,
            'latest_sales':latest_sales,
            'new_products':new_products,
            'new_users':new_users,
            'new_sales':new_sales,
            'new_invoices':sales_total_amount,
            'all_users':all_users,
            'growth_user':growth_user,
            'new_users_percent':new_users_percent,
            'last_users':last_users,
            'this_week_sales_amount':this_week_sales_amount,
            'last_week_sales_amount':last_week_sales_amount,
        })


class AdminProductBrandView(ListView):
    template_name="admin_panel_module/product_module/product_brands.html"
    model=ProductBrand
    context_object_name='product_brands'
    # ordering=['-title']
    paginate_by=6
    form_class=ProductBrandAdminForm

    def post(self,request):
        # todo: add empty value for filter brand for title
        # print(request.POST)
        if 'add-new-brand' in request.POST:
            form=self.form_class(request.POST)
            if form.is_valid() and form.cleaned_data['title'] != '':
                cd=form.cleaned_data
                new_brand=ProductBrand(title=cd['title'],is_active=cd['is_active'])
                new_brand.save()
                brands=ProductBrand.objects.all()
                messages.success(request,'brand added successfully','success')
                return render(request,self.template_name,{
                    'product_brands':brands,
                    'form':self.form_class()
                })


        elif 'filter-brand' in request.POST:
            form=self.form_class(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                brands=ProductBrand.objects.filter(title__iexact=cd['title'],is_active=cd['is_active'])
                return render(request,self.template_name,{
                    'form':self.form_class(),
                    'product_brands':brands
                })
            else:
                return HttpResponse('invalid-data-form')
            
        elif 'search-brand' in request.POST:
            form=self.form_class(request.POST)
            if form.is_valid():
                cd=form.cleaned_data
                brands=ProductBrand.objects.filter(title__icontains=cd['title'],is_active=cd['is_active'])
                return render(request,self.template_name,{
                    'form':self.form_class(),
                    'product_brands':brands
                })
            else:
                return HttpResponse('invalid-data-form')
        
        return HttpResponse('invalid-data-form')

    def get_queryset(self):        
        query=super().get_queryset()
        return query
    
    def get_context_data(self, **kwargs):
        '''
            if need to pass new data in product template and
            this is not product model must send with this method and override this
        '''
        # context=super().get_context_data(**kwargs) 
        context = super(AdminProductBrandView, self).get_context_data(**kwargs)
        context['form']=self.form_class()
        return context
    

def admin_product_brand_delete(request,brand_id):
    target_brand=get_object_or_404(ProductBrand,id=brand_id)

    if target_brand is not None:
        target_brand.delete()
        messages.success(request,'brand deleted successfully','success')
        return redirect(reverse('admin-product-brands'))
    else:
        messages.error(request,'this brand does not exists!!','danger')
        return redirect(reverse('admin-product-brands'))

    
class EditProductBrandAdminView(View):
    template_name='admin_panel_module/product_module/product_brand_detail.html'
    form_class=ProductBrandAdminModelForm

    def dispatch(self, request,brand_id, *args, **kwargs):
        self.target_brand=get_object_or_404(ProductBrand,id=brand_id)
        return super().dispatch(request, *args, **kwargs)
    

    def get(self,request):
        if self.target_brand is not None:
            return render(request,self.template_name,{
                'brand':self.target_brand,
                'form':self.form_class(instance=self.target_brand)
            })


    def post(self,request):
        form=self.form_class(request.POST,instance=self.target_brand)
        if form.is_valid():
            form.save()
            messages.success(request,'brand edited successfully','success')
            return redirect(reverse('admin-product-brands'))
        else:
            return redirect(reverse('admin-product-brands'))











