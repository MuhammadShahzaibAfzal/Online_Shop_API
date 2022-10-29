from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/products")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    numberOfReviews = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    isPaid = models.BooleanField(default=False)
    paidAt= models.DateTimeField(auto_now_add=False,null=True,blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt =models.DateTimeField(auto_now_add=False,null=True,blank=True) 
    createdAt = models.DateTimeField(auto_now_add=True)




class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.id
    
