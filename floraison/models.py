from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class user_address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal = models.IntegerField()
    contact_phone = PhoneNumberField()

    def __str__(self):
        return self.address_1

    class Meta():
        verbose_name_plural = 'Addresses'

class order(models.Model):
    total = models.FloatField(max_length=200)
    paid = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    delivery = models.ForeignKey(user_address, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta():
        verbose_name_plural = 'Categories'

class cake_type(models.Model):
    name = models.CharField(max_length=50)
    modifier = models.FloatField(default=0)

    def __str__(self):
        return self.name

class cookie_type(models.Model):
    name = models.CharField(max_length=200)
    modifier = models.FloatField(default=0)

    def __str__(self):
        return self.name

class frosting(models.Model):
    name = models.CharField(max_length=50)
    modifier = models.FloatField(default=0)

    def __str__(self):
        return self.name

class filling(models.Model):
    name = models.CharField(max_length=50)
    modifier = models.FloatField(default=0)

    def __str__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    starting_price = models.FloatField()
    description = models.CharField(max_length=200)
    days_required = models.IntegerField()
    cake_type = models.ForeignKey(cake_type, on_delete=models.CASCADE) 
    cookie_type = models.ForeignKey(cookie_type, on_delete=models.CASCADE)
    frosting = models.ForeignKey(frosting, on_delete=models.CASCADE)
    filling = models.ForeignKey(filling, on_delete=models.CASCADE)
    image = models.FileField(upload_to='./images/', default='None')
    photo = models.ImageField(upload_to='images/')
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class order_item(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    unit_price = models.FloatField()
    message = models.CharField(max_length=50, null=True)
    special_instructions = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.item