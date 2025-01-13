from django.urls import path
from . import views

urlpatterns = [
    path('checkout-session/',views.checkout, name="checkout_session"),
    path('success/',views.payment_success,name='payment_success'),
    path('cancel/',views.payment_cancel,name='payment_cancel')
]
