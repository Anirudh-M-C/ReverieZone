from django.shortcuts import render
from .models import Order,Ordereditem

# Create your views here.
from django.shortcuts import render

# Create your views here.
def show_cart(request):
    
    return render(request,'cart.html')

def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=request.POST.get('quantity')
        product_id=request.POST.get('product_id')
        cart_obj=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )