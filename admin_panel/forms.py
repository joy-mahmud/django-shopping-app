from django import forms 
from main.models import Product

class AddProduct(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','price','quantity','image']