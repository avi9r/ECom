from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import Customer, Product,  Category
# Create your views here.
def index(request):
    context={}
    return render(request, 'index.html', context)

def contact(request):
    context={}
    return render(request, 'contact.html', context)

def cart(request):
    context={}
    return render(request, 'cart.html', context)

def register(request):
    if request.method == 'POST':
        
        data = Customer()
        data.fname = request.POST['fname']
        data.lname = request.POST['lname']
        data.email = request.POST['email']
        data.mobile = request.POST['mobile']
        data.password = request.POST['password']  
        data.save()
        messages.success(request,"You Are Registered Sucessfully.")

        return redirect('login')      
    else:   
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        try:
            data = Customer.objects.get(email = request.POST['email'], password = request.POST['password'])
            request.session['username'] = data.fname
            return redirect('home')
        except Customer.DoesNotExist as e:
            messages.success(request, 'Email / Password invalid...!')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    try:
        del request.session['username']
        return redirect('home')
    except:
        return render(request, 'login')


def account(request):
    context={}
    return render(request, 'my-account.html', context)

def product_list(request):
    context={}
    return render(request, 'product-list.html', context)

def wishlist(request):
    context={}
    return render(request, 'wishlist.html', context)

def checkout(request):
    context={}
    return render(request, 'checkout.html', context)


