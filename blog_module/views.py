from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Article,ArticleCategory


class ArticleView(View):
    template_name='blog_module/articles.html'

    def get(self,request):
        articles=Article.objects.filter(is_active=True).order_by('-created_date')
        return render(request,self.template_name,{
            'articles':articles
        })
    
    def post(self,request):
        pass

class ArticleDetailView(View):
    template_name='blog_module/article_detail.html'

    def get(self,request,slug):
        article=get_object_or_404(Article,slug=slug)

        return render(request,self.template_name,{
            'article':article
        })

    def post(self,request):
        pass
