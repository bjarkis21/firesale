from django.contrib.auth.models import User
from django.db import models
#from user.models import UserProfile
from datetime import datetime



# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Condition(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    #condition = models.CharField(max_length=255, default="", blank=True, null=True)
    condition = models.ForeignKey(Condition, on_delete=models.SET_DEFAULT, default=1)
    image = models.CharField(max_length=500, blank=True)
    reserve = models.PositiveIntegerField(default=100)#blank=True, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    creation_date = models.DateTimeField(default=datetime.now)
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, related_name='buyer', null=True)
    rating = models.FloatField(blank=True, null=True)
    buy_date = models.DateTimeField(blank=True, null=True)
    isPaid = models.BooleanField(default=False)
    isSold = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title


class BidsOn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bidson')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='bidson')
    amount = models.PositiveIntegerField()
    bid_date = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'advertisement', 'amount'], name='keyConstraint')
        ]

    def __str__(self):
        return f"{str(self.user)}, {self.advertisement.title}, {str(self.amount)}"
