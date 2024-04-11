from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_product(request):
    product_list=Product.objects.all()
    context={
        'product':product_list
    }
    return render(request,'products.html',context)

def product_detail(request):
    return render(request,'product_details.html')