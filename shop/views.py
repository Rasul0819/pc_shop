from django.shortcuts import render, get_object_or_404,redirect
from cart.forms import CartAddProductForm
from .models import Category, Product,CustomUser,Rating
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import RatingForm

from django.http import JsonResponse


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

def loginuser(request,category_slug=None):
    if request.method == 'GET':
        return render(request,'loginuser.html',{'form':AuthenticationForm()})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'shop/loginuser.html',{'form':AuthenticationForm(),'error':'Qollaniwshi ati ya parol qate'})
        else:
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
                      'products': products,
                      'username':request.POST['username']

                  })



def rate_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            user = request.user

            # Создаем объект оценки
            Rating.objects.create(user=user, product=product, rating=rating)
            
            # Можно добавить дополнительные действия после создания оценки, например, перенаправление на страницу товара
            return redirect('shop:product_detail', id=product.id, slug=product.slug)
    else:
        form = RatingForm()

    return render(request, 'rate_product.html', {'form': form, 'product': product})
# def signupuser(request):
#     if request.method == 'GET':
#         return render(request,'shop/signupuser.html',{'form':UserCreationForm(),})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             user=User.objects.create_user(request.POST['username'],password = request.POST['password1'])
#             user.save()
#             return redirect(request,'shop/loginuser.html')
#         else:
#             return render(request,'shop/signupuser.html',{'form':UserCreationForm(),'error':'Parol ya username qate'})




# def signupuser(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             # Создание и сохранение нового пользователя
#             form.save()
#             return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})


