from django import template

register=template.Library()

@register.filter(name='rowssplit')
def rowssplit(list_data,rowssplit_size):
    rowssplit=[]
    i=0
    for data in list_data:
        rowssplit.append(data)
        i=i+1
        if i==rowssplit_size:
            yield rowssplit
            i=0
            rowssplit=[]
    if rowssplit:
        yield rowssplit