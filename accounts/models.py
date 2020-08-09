from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    profile_pic = models.ImageField(default="1200px-Circle-icons-profile.svg.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    CATEGORY = (
        ("INDOOR", "INDOOR"),
        ("OUTDOOR", "OUTDOOR"),
    )

    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ("PENDING", "PENDING"),
        ("OUT OF DELIVERY", "OUT OF DELIVERY"),
        ("DELIVERED", "DELIVERED"),
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, null=True, choices=STATUS)
    note = models.CharField(max_length=1020, null=True)

    def __str__(self):
        return self.product.name
