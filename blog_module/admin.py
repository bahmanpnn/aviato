from typing import Any
from django.contrib import admin
from .models import Article,ArticleCategory,ArticleTag,ArticleComment,ArticleVisit


class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','author','is_active']
    list_filter=['author','is_active']

    def save_model(self, request: Any, obj: Any, form: Any, change: Any):
        if not change:
            obj.author=request.user
        return super().save_model(request, obj, form, change)


class ArticlVisitAdmin(admin.ModelAdmin):
    list_display=['__str__','article','user','ip','article_id']

admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleVisit,ArticlVisitAdmin)
admin.site.register(ArticleCategory)
admin.site.register(ArticleTag)
admin.site.register(ArticleComment)