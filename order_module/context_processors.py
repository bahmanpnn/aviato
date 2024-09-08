from .models import OrderBasket


def basket_products(request):
    user_basket,is_created=OrderBasket.objects.prefetch_related('order_detail').get_or_create(is_paid=False,user_id=request.user.id)
    return {'user_basket':user_basket}