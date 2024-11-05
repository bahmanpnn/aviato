from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Count
from home_module.models import UserEmailSubscribe
from utils.http_service import get_client_ip
from .models import Article,ArticleCategory,ArticleComment,ArticleVisit
from .forms import UserEmailSubscribeForm
from permissions import is_authenticated_permission

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
        # context=super().get_context_data(**kwargs) 
        context = super(ArticleView, self).get_context_data(**kwargs)
        most_viewed_articles=Article.objects.filter(is_active=True).annotate(visit_count=Count('articlevisit')).order_by('-visit_count')[:5]
        context['form'] = UserEmailSubscribeForm() 
        context['most_viewed_articles']=most_viewed_articles
        return context
    
    def post(self, request):
        form = UserEmailSubscribeForm(request.POST)
        if form.is_valid():
            new_email=UserEmailSubscribe(email=form.cleaned_data.get('email'))
            new_email.save()
            messages.success(request,'Thank You,We received your email successfully')
            return redirect(reverse('articles'))
        
        messages.warning(request,'please enter a valid email address!!')
        return redirect(reverse('articles'))
        
        
class ArticleDetailView(View):
    template_name='blog_module/article_detail.html'

    def get(self,request,slug):
        article=get_object_or_404(Article,slug=slug,is_active=True)
        comments=ArticleComment.objects.filter(parent_id=None,article_id=article.id).order_by('-created_date').prefetch_related('articlecomment_set')
        comments_count=ArticleComment.objects.filter(article_id=article.id).count()
        
        # product visit adding and get user ip
        user_ip=get_client_ip(request)        
        has_been_visited=ArticleVisit.objects.filter(ip__exact=user_ip,article=article).exists()

        if not has_been_visited:
            if request.user.is_authenticated:
                user_id=request.user.id
            else:
                user_id=None
            new_visit=ArticleVisit(ip=user_ip,article=article,user_id=user_id)
            new_visit.save()

        return render(request,self.template_name,{
            'article':article,
            'comments':comments,
            'comments_count':comments_count
        })


def categories(request):
    template_name='blog_module/components/article_category.html'
    categories=ArticleCategory.objects.filter(is_active=True)

    return render(request,template_name,{
        'categories':categories
    })


@is_authenticated_permission
def add_article_comment(request):
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






'''
    combine form view with list view cbv ***
'''
# from django.http import Http404
# from django.views.generic import ListView
# from django.views.generic.edit import FormMixin
# from django.utils.translation import ugettext as _

# class FormListView(FormMixin, ListView):
#     def get(self, request, *args, **kwargs):
#         # From FormMixin
#         form_class = self.get_form_class()
#         self.form = self.get_form(form_class)

#         # From ListView
#         self.object_list = self.get_queryset()
#         allow_empty = self.get_allow_empty()
#         if not allow_empty and len(self.object_list) == 0:
#             raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
#                           % {'class_name': self.__class__.__name__})

#         context = self.get_context_data(object_list=self.object_list, form=self.form)
#         return self.render_to_response(context)

#     def post(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)