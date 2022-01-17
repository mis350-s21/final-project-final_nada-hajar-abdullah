from django.db import models


 
# Create your models here.

class Customer(models.Model):
  #cus_id = models.CharField("Customer ID", max_length=12, null=False, unique=True, default=0)
  name = models.CharField("Customer Name", max_length=50, null=False)
  email = models.EmailField(max_length=50)
  #address = models.CharField("Customer Address", max_length=100, null=True)
  

  def __str__(self):
    return f"{self.name}"

class Product(models.Model):
  Choice=(
    (0, "Apple Iphone 11"),
    (1, "Apple Iphone 12"),
    (2, "Samsung 10"),
    (3, "Sony 13"),
  )

  product = models.CharField("Product ID", max_length=10, null=False, unique=True)
  model = models.IntegerField("Phone Model", null=True, choices=Choice)
  price = models.IntegerField(default=0)
  purchased_on = models.DateField("Purchased Date", null=True)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=False)

  def __str__(self):
    return f"Model: {self.model} - Customer: {self.customer} - Product: {self.product}"


class feedback(models.Model):
    customer_name=models.CharField(max_length=50)
    feedback=models.TextField()
    Product=models.ForeignKey('Product',on_delete= models.CASCADE)
