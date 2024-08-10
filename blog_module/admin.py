from django.contrib import admin
from .models import Article,ArticleCategory,ArticleTag

admin.site.register(Article)
admin.site.register(ArticleCategory)
admin.site.register(ArticleTag)