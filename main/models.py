from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.FileField(upload_to='uploads/',null=True)
    
class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)

class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items',null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cart_items',null=True)
    quantity=models.PositiveIntegerField(default=1)