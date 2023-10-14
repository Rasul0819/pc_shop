from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout
from cart.forms import CartAddProductForm
from .models import Category, Product,CustomUser
from .forms import SignUpForm, LoginForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,'cart_product_form':cart_product_form })

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        cd = form.cleaned_data
        username = cd['username']
        password = cd['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

# from django.urls import reverse

# def login(request):
#     return render(request,'login.html')
