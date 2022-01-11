from django.db import models
from django.contrib.auth.models import User

 #Create your models here.
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


class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    order_date=models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.id}"       


class feedback(models.Model):
    customer_name=models.CharField(max_length=50)
    feedback=models.TextField()
    Product=models.ForeignKey('Product',on_delete= models.CASCADE)
