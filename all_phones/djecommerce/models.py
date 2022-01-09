from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price= models.FloatField()
    category= models.CharField(max_length=200)
    description= models.TextField()
    image= models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"


class feedback(models.Model):
    customer_name=models.CharField(max_length=50)
    feedback=models.TextField()
    Product=models.ForeignKey('Product',on_delete= models.CASCADE)