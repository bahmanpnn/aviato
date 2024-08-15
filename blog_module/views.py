from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import ListView
from .models import Article,ArticleCategory,ArticleComment


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
        article=get_object_or_404(Article,slug=slug,is_active=True)
        comments=ArticleComment.objects.filter(parent_id=None,article_id=article.id).order_by('-created_date').prefetch_related('articlecomment_set')
        comments_count=ArticleComment.objects.filter(article_id=article.id).count()
        
        return render(request,self.template_name,{
            'article':article,
            'comments':comments,
            'comments_count':comments_count
        })

    def post(self,request):
        pass


def categories(request):
    template_name='blog_module/components/article_category.html'
    categories=ArticleCategory.objects.filter(is_active=True)

    return render(request,template_name,{
        'categories':categories
    })


def add_article_comment(request):
    print(request.GET)

    if request.user.is_authenticated:
        article_id=request.GET.get('article_id')
        parent_id=request.GET.get('parent_id')
        comment_text=request.GET.get('comment')
        new_comment=ArticleComment(parent_id=parent_id,article_id=article_id,text=comment_text,author_id=request.user.id)
        new_comment.save()

        comments=ArticleComment.objects.filter(article_id=article_id,parent_id=None).order_by('-created_date').prefetch_related('articlecomment_set')
        comments_count=ArticleComment.objects.filter(article_id=article_id).count()


        return render(request,'blog_module/includes/article_comments.html',{
            'comments':comments,
            'comments_count':comments_count
        })

    return HttpResponse('got response succussfully')
