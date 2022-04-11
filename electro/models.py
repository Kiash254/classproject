from pyexpat import model
from tkinter import CASCADE
from django.db import models
from pydantic import NoneIsAllowedError
from sqlalchemy import null
from django.contrib.auth.models import User

# Create your models here.


class Usertable(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    fname=models.CharField(max_length=20,blank=True)
    lname=models.CharField(max_length=20,blank=True)
    age=models.IntegerField()

    def __str__(self):
        return f'fname{self.fname},lname{self.lname}'



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return (self.title)


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"