from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_product(request):
    product_list=Product.objects.all()
    page=request.GET.get('page',1)
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context={
        'product':product_list
    }
    return render(request,'products.html',context)

def product_detail(request):
    return render(request,'product_details.html')