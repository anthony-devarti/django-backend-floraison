from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal = models.IntegerField()
    contact_phone = models.IntegerField()

class order(models.Model):
    total = models.FloatField(max_length=200)
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    delivery = models.ForeignKey(user_address, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class category(models.Model):
    name= models.CharField(max_length=50)

class cake_type(models.Model):
    name = models.CharField(max_length=50)
    modifier = models.FloatField(default=0)

class cookie_type(models.Model):
    name = models.CharField(max_length=200)
    modifier = models.FloatField(default=0)

class frosting(models.Model):
    name = models.CharField(max_length=50)
    modifier = models.FloatField(default=0)

class filling(models.Model):
    name = models.CharField(max_length=50)
    modifier = models.FloatField(default=0)

class item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    starting_price = models.FloatField()
    message = models.CharField(max_length=50)
    days_required = models.IntegerField()
    cake_type = models.ForeignKey(cake_type, on_delete=models.CASCADE)
    cookie_type = models.ForeignKey(cookie_type, on_delete=models.CASCADE)
    frosting = models.ForeignKey(frosting, on_delete=models.CASCADE)
    filling = models.ForeignKey(filling, on_delete=models.CASCADE)
    published = models.BooleanField(default=True)

class order_item(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    unit_price = models.FloatField()