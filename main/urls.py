from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('addProduct/',views.add_product, name="add_product"),
    path('productDetails/<int:id>', views.product_details, name='product_details'),
    #path('addToCart/',views.add_to_cart, name="add_to_cart"),
    path('addToCart/<int:product_id>',views.add_to_cart, name="add_to_cart"),
    path('cart/',views.view_cart, name="cart"),
]
