from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('addProduct/',views.add_product, name="add_product"),
    path('productDetails/<int:id>', views.product_details, name='product_details'),
    path('addToCart/',views.add_to_cart, name="add_to_cart")
]
