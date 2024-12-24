from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AddProduct
from .models import Product,Cart
from django.views.decorators.csrf import csrf_exempt
import json

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

def product_details(request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product
        
    }
    
    return render(request,'main/product_details.html',context)

@csrf_exempt
def add_to_cart(request):
    # id=request.GET.get('product_id')
    if request.method=="POST":
        body=json.loads(request.body)

        product_id=body.get('product_id')
        cart=Cart(product_id=product_id)
        cart.save()
        return HttpResponse('product  added to cart successfully')
    # cart=Cart(product_id=id)
    # cart.save()
    
    