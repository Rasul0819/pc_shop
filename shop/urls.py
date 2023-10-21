from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    
    path('', views.product_list, name='product_list'),
    path('loginuser/',views.loginuser,name='loginuser'),
    # path('rate/<int:product_id>/<slug:slug>/', views.rate_product, name='rate_product'),
     

#     path('signupuser/',views.signupuser,name='signupuser'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('rate/<int:id>/<slug:slug>/', views.rate_product, name='rate_product'),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),

     
]