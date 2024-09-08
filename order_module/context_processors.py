from .models import OrderBasket


def basket_products(request):
    user_basket=OrderBasket.objects.prefetch_related('order_detail').filter(is_paid=False,user_id=request.user.id).first()
    
    if user_basket is not None:
        return {'user_basket':user_basket}
    else:
        return {'user_basket':None}
