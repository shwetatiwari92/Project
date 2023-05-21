from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def seller_register(request):
    if request.method == 'POST':
        # if request.POST['password'] == request.POST['repassword']:
        Seller.objects.create(
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            pic = request.FILES['pic'],
            password = request.POST['password'],
            gst_no = request.POST['gst_no']
        )
        return render(request, 'seller_register.html', {'smessage': 'Successfully created!!'})
    else:
        return render(request, 'seller_register.html')
    

def seller_login(request):
    if request.method == 'GET':
        return render(request, 'seller_login.html')
    else:
        #without any validations, direct login
        request.session['seller_email'] = request.POST['email']
        return redirect('seller_index')
    

def seller_index(request):
    try:
        s1 = Seller.objects.get(email = request.session['seller_email'])
        s_l = SellerOrderHistory.objects.filter(product__seller = s1)
        return render(request, 'seller_index.html', {'sellerdata': s1, 'my_orders': s_l})
    except:
        return redirect('seller_login')
    

def seller_logout(request):
    del request.session['seller_email']
    return redirect('seller_login')


def add_product(request):
    try:
        s1 = Seller.objects.get(email = request.session['seller_email'])
        if request.method == 'GET':
            return render(request, 'add_product.html', {'sellerdata': s1})
        else:
            Product.objects.create(
                name = request.POST['product_name'],
                des = request.POST['des'],
                price = request.POST['price'],
                pic = request.FILES['pic'],
    
                seller = s1  #s1 Seller class ka obj hai, because ye ForeignKey field hai
            )
            return render(request, 'add_product.html', {'sellerdata': s1, 'msg': 'Successfully Created'})
    except:
        return redirect('seller_login')
    

def seller_profile(request):
    if request.method == 'GET':
        try:
            s1 = Seller.objects.get(email = request.session['seller_email'])
            seller_f_obj = SellerForm(instance= s1)
            return render(request, 'seller_profile.html', {'sellerdata': s1, 'form': seller_f_obj})
        except:
            return redirect('seller_login')
    else:
        s1 = Seller.objects.get(email = request.session['seller_email'])
        s1.full_name = request.POST['full_name']
        s1.gst_no = request.POST['gst_no']
        s1.pic = request.FILES['pic']
        s1.save() #ye line pe se database mein value update hogi
        return redirect('seller_profile')




    


        # seller_f_obj = SellerForm(data= request.POST, instance= s1)
        # if seller_f_obj.is_valid():
        #     seller_f_obj.save()
        #     return redirect('seller_index')
        # else:
        #     s1 = Seller.objects.get(email = request.session['seller_email'])
        #     seller_f_obj = SellerForm(instance= s1)
        #     return render(request, 'seller_profile.html', {'sellerdata': s1, 'form': seller_f_obj, 'msg': 'Some Problem'})