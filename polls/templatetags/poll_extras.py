from django import template
from user_profile_module.models import UserFavoriteProduct
from blog_module.models import ArticleTag,Article,ArticleComment

register=template.Library()

@register.filter(name='three_digits')
def three_digits(value:int):
    return '{:,}'.format(value)


@register.simple_tag
def check_modulo(value1,value2=2,*args, **kwargs):
    return int(value1) % int(value2)


# @register.simple_tag
# def check_is_favorite(product,user):
#     return UserFavoriteProduct.objects.filter(product=product,user=user).exists()
# for using simple tags{% check_is_favorite product.id user.id %}


@register.filter
def is_favorite_product(product_id, user_id):
    return UserFavoriteProduct.objects.filter(product_id=product_id, user_id=user_id).exists()


@register.simple_tag
def article_comments_count(article_id):
    article_comments=ArticleComment.objects.filter(article_id=article_id).count()
    return article_comments
