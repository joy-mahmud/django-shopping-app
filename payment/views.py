from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
# Create your views here.
from django.conf import settings

stripe.api_key=settings.STRIPE_SECRET_KEY

@csrf_exempt
def checkout(request):
    if request.method=="POST":
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data':{
                        'currency':'usd',
                        'product_data':{
                            'name':'Product name',
                        },
                        'unit_amount':5000
                    },
                    'quantity':1,
                }
            ],
            mode="payment",
            success_url="http://127.0.0.1:8000/payment/success/",
            cancel_url="http://127.0.0.1:8000/payment/cancel/",
        )
        return JsonResponse({'id':checkout_session.id})
    return HttpResponse("payment gateway")

def payment_success(request):
    return render(request,'payment/success.html')

def payment_cancel(request):
    return render(request,'payment/cancel.html')