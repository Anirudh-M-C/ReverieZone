from django import template

register=template.Library()

@register.filter(name='rowsplit')
def rowsplit(list,rowsplit_size):
    