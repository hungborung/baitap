from django.db import models
from app.models import *
# Create your models here.

class Order(models.Model):
    class Status:
        NEW = 0
        DELIVERED = 1
        CANCELED = 2

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.FloatField(blank=True, null=True)
    used_coupon = models.CharField(max_length=50, blank=True, null=True)
    payment_intent = models.CharField(max_length=255, blank=True, null=True)
    deliver_date = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return '%s' % self.first_name

    class Meta:
        ordering = ('-create_at',)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id