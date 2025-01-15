from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from .models import Payment
from main.models import Cart
# Create your views here.
from django.conf import settings

stripe.api_key=settings.STRIPE_SECRET_KEY

@csrf_exempt
def checkout(request):
    if request.method=="POST":
        data=json.loads(request.body)
        amount= int(data.get('amount'))
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data':{
                        'currency':'usd',
                        'product_data':{
                            'name':'Total Price',
                        },
                        'unit_amount':amount*100
                    },
                    'quantity':1,
                }
            ],
            mode="payment",
            success_url=f"http://127.0.0.1:8000/payment/success/?amount={amount}",
            cancel_url="http://127.0.0.1:8000/payment/cancel/",
        )
        return JsonResponse({'id':checkout_session.id})
    return HttpResponse("payment gateway")

def payment_success(request):
    amount=request.GET.get('amount')
    userId= request.user.id
    userEmail = request.user.email
    payment = Payment.objects.create(user_id=userId,user_email=userEmail,amount=amount)
# to less the product quantity
    cart = Cart.objects.get(user=request.user)
    cart_items= cart.items.all()
    for item in cart_items:
        product = item.product
        if product.quantity >= item.quantity:
            product.quantity -= item.quantity
            product.save()
        else:
            return HttpResponse("Not enough stock fot the product", product.name)
    # to clear the cart
    cart.items.all().delete()
    
    return render(request,'payment/success.html')

def payment_cancel(request):
    return render(request,'payment/cancel.html')