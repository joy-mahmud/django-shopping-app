from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from main.models import Product
from .forms import AddProduct,UpdateProduct
# Create your views here.
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)  
def dashboard(request):
    products=Product.objects.all()
    return render(request,'admin_panel/dashboard.html',{'products':products})

@login_required
@user_passes_test(is_admin)
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

@login_required
@user_passes_test(is_admin)
def update_product(request,id):
    product= Product.objects.get(id=id)
    if request.method=="POST":
        form=UpdateProduct(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UpdateProduct(instance=product)
    return render(request,'admin_panel/update_product.html',{'form':form,'product':product})    

@login_required
@user_passes_test(is_admin)
def delete_product(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        product.delete()
        return redirect('dashboard')
    return render(request,'admin_panel/confirm_delete.html',{'product':product})
    