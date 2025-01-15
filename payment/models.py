from django.db import models

# Create your models here.
class Payment(models.Model):
    user_id=models.IntegerField()
    amount=models.IntegerField()
    user_email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)