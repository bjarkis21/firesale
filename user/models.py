from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
from ads.models import Advertisement


class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='checkout', default='')
    advertisement = models.OneToOneField(Advertisement, on_delete=models.CASCADE, related_name='checkout', default='')
    fullname = models.CharField(max_length=255)
    #country = models.CharField(max_length=255)
    country = CountryField()
    city = models.CharField(max_length=255)
    #city = CountryField(default=1)
    postcode = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    street_no = models.CharField(max_length=255)
    credid_card_fullname = models.CharField(max_length=255, default="")
    credid_card_number = models.CharField(max_length=16)
    credid_card_cvc = models.CharField(max_length=4)
    credid_card_expiration_date = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.street}, {self.street_no}"


class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', related_name='userprofile',
                                primary_key=True)
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    rating = models.FloatField(blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=9999, blank=True)
    ssn = models.CharField(max_length=10, blank=True)
    bank = models.CharField(max_length=10, blank=True)
    hb = models.CharField(max_length=10, blank=True)
    account_no = models.CharField(max_length=20, blank=True)
    profile_image = models.CharField(max_length=9999, blank=False, default='https://static.vecteezy.com/system/resources/previews/002/318/271/original/user-profile-icon-free-vector.jpg')
    isNewMessage = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    isSeen = models.BooleanField(default=False)
