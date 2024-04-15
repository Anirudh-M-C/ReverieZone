from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_account,name='show_account'),
    path('logout_user/',views.logout_user,name='logout_user'),
]