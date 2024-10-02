from django import template

register=template.Library()

@register.filter(name='three_digits')
def three_digits(value:int):
    return '{:,}'.format(value)


@register.simple_tag
def check_modulo(value1,value2=2,*args, **kwargs):
    return int(value1) % int(value2)
