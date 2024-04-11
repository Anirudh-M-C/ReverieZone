from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('list_product/',views.list_product,name="list_product"),
    path('product_detail/',views.product_detail,name='product_detail'),

]