from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView
from .models import Article,ArticleCategory


class ArticleView(ListView):
    template_name='blog_module/articles.html'
    model=Article
    context_object_name='articles'
    ordering=['-created_date']
    paginate_by=1

    def get_queryset(self):        
        query=super().get_queryset().filter(is_active=True)
        
        if self.kwargs:
            category=self.kwargs.get('category')
            if category is not None:
                query=query.filter(category__url_title__iexact=category,is_active=True)

        return query
    
    def get_context_data(self, **kwargs):
        '''
            if need to pass new data in product template and
            this is not product model must send with this method and override this
        '''
        context=super().get_context_data(**kwargs)      

        return context


class ArticleDetailView(View):
    template_name='blog_module/article_detail.html'

    def get(self,request,slug):
        article=get_object_or_404(Article,slug=slug)

        return render(request,self.template_name,{
            'article':article
        })

    def post(self,request):
        pass


def categories(request):
    template_name='blog_module/components/article_category.html'
    categories=ArticleCategory.objects.filter(is_active=True)

    return render(request,template_name,{
        'categories':categories
    })

