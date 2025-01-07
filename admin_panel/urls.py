from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addProduct/',views.add_product, name="add_product"),
]
