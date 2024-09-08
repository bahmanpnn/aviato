from django import template

register=template.Library()

@register.filter(name='three_digits')
def three_digits(value:int):
    return '{:,}'.format(value)


# @register.simple_tag
# def multiply(price,count,*args, **kwargs):
#     return three_digits(price*count)