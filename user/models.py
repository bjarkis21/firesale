from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    street_no = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street}, {self.street_no}"


class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    #email = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, blank=True)
    rating = models.FloatField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    description = models.CharField(max_length=9999, blank=True)
    ssn = models.CharField(max_length=10, blank=True)
    bank = models.CharField(max_length=10, blank=True)
    hb = models.CharField(max_length=10, blank=True)
    account_no = models.CharField(max_length=20, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


