from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('addProduct/',views.add_product, name="add_product")
]
