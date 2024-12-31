from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import AddProduct
from .models import Product,Cart,CartItem
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum,F

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
        product = Product.objects.get(id=product_id)
        cart,created = Cart.objects.get_or_create(user=request.user)
        print(created)
        
        cart_item,item_created= CartItem.objects.get_or_create(cart=cart,product=product)
        print('item created',item_created)
        if not item_created :
            cart_item.quantity+=1
            cart_item.save()
            
        return JsonResponse({'redirect_url':'http://127.0.0.1:8000/cart/'})
    # cart=Cart(product_id=id)
    # cart.save()
    
def view_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    items=cart.items.select_related('product').annotate(
        item_total=F('quantity') * F('product__price')
    )
    
    total_price = items.aggregate(total=Sum('item_total'))['total'] or 0

    return render(request,'main/view_cart.html',{'items':items,'total_price':total_price})
    
    