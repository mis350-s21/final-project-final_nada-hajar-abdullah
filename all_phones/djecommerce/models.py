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
    Choice=(
    (0, "Apple Iphone 11"),
    (1, "Apple Iphone 12"),
    (2, "Samsung 10"),
    (3, "Sony 13"),
  )

    #product= models.CharField("Product ID",max_length=12,null=False,unique=True)
    model = models.IntegerField("Phone Model", null=True, choices=Choice) 
    price= models.IntegerField(default=0)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=False,default="0")
    def __str__(self):
        return f"{self.model}"

class feedback(models.Model):
    customer_name=models.CharField(max_length=50)
    feedback=models.TextField()
    Product=models.ForeignKey('Product',on_delete= models.CASCADE)
