from email.headerregistry import Address
from tkinter import CASCADE
from typing import cast
from django.db import models


 
# Create your models here.

class Customer(models.Model):
    name= models.CharField("Customer Name", max_length=50,null=False)
    email= models.EmailField(max_length=50)
    #address= models.CharField("Customer Address",max_length=100, null=True)

    def __str__(self):
        return f"{self.name}"   
   

class Product(models.Model):
    

    title= models.CharField(max_length=200,default=0)
    price= models.IntegerField(default=0)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=False,default="0")
    description=models.TextField(default=0)
    image=models.CharField(max_length=300, default=0)
    def __str__(self):
        return f"{self.title}"

class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE,null=False,default=0)        
    date_ordered=models.DateField("Date of Order", null=True)
    shipping_address=models.TextField(default=0)
    def __str__(self):
        return f"{self.id}"

class feedback(models.Model):
    customer_name=models.CharField(max_length=50)
    feedback=models.TextField()
    Product=models.ForeignKey('Product',on_delete= models.CASCADE)
