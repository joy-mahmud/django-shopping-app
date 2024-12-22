from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AddProduct
from .models import Product
# Create your views here.
def home(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    
    return render(request,'main/home.html',context)


def add_product(request):
    if request.method=="POST":
        form=AddProduct(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect("home")
    
    form=AddProduct()
    context={
        'form':form
    }
    return render(request,'main/addProduct.html',context)
