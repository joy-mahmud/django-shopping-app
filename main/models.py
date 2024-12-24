from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.FileField(upload_to='uploads/',null=True)
    
class Cart(models.Model):
    product_id=models.IntegerField(null=True,blank=True)