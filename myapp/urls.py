
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('ashwini/', fun1, name="ashwini"),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('register/', register, name='shweta'),
    path('login/', login, name='login'),
    path('otp/', otp, name='otp'),
    path('contact/', contact, name='contact'),
    path('faqs/', faqs, name='faqs'),
    path('logout/', logout, name='logout'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('del_cart_row/<int:cid>', del_cart_row, name='del_cart_row'),
    path('start_payment/', homepage, name='start_payment'),
    path('start_payment/paymenthandler/', paymenthandler, name='paymenthandler'),





]