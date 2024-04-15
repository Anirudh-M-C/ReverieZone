from django.shortcuts import render,redirect
from .state import STATE_CHOICES
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def logout_user(request):
     logout(request)
     return redirect('/')
def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            state=request.POST.get('state')
            city=request.POST.get('city')
            phone=request.POST.get('phone')
            location=request.POST.get('location')
            pincode=request.POST.get('pincode')
            
            # create user account
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create customer account
            customer=Customer.objects.create(
                user=user,
                phone=phone,
                address=address,
                pincode=pincode,
                location=location,
                city=city,
                state=state
            )
            return redirect('/')
        except Exception as e:
            error_message=f"duplicate username {e}"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if user:
                 login(request,user)
                 return redirect('/')
            else:
                messages.error(request,'invalid user credentials')
    context = {
        'STATE_CHOICES': STATE_CHOICES,
    }
    return render(request, 'account.html', context)