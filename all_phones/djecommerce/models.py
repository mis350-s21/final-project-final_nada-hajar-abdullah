from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length = 254)
    def __str__(self):
        return f"{self.name}"
        
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price= models.FloatField()
    category= models.CharField(max_length=200)
    description= models.TextField()
    image= models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"