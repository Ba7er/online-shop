from django.db import models
from django.conf import settings
# Create your models here.
from prod_cat_app.models import Products
from registration_app.models import Myuser
import random


User = settings.AUTH_USER_MODEL



class Cart(models.Model):
    product = models.ManyToManyField(Products, blank=True)
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total   = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ShippingAddresses(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    cart        = models.OneToOneField(Cart,primary_key=True, on_delete=models.CASCADE)
    city        = models.CharField(max_length=50)
    area        = models.CharField(max_length=50)
    address_line= models.CharField(max_length=150)
    Pobox = models.IntegerField()

    def __str__(self):
        return str(self.city)




class My_order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping_details = models.ForeignKey(ShippingAddresses, on_delete=models.CASCADE)
    order_id = models.BigIntegerField('Order Number')
    order_date = models.DateTimeField()
    order_status = models.BooleanField('Dlivered',null=True)

    def __str__(self):
        return str(self.order_id)





    # def save(self,request):
    #     if request.user.is_authenticated():
    #         self.
