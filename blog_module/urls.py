from django.urls import path
from . import views


urlpatterns = [
    path('',views.ArticleView.as_view(),name='articles'),
    path('category/<str:category>',views.ArticleView.as_view(),name='articles-by-category'),
    path('add-comment/article_comment/',views.add_article_comment,name='add-article-comment'),
    path('<slug:slug>/',views.ArticleDetailView.as_view(),name='article-detail'),
]
