from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    profilepic=models.ImageField(upload_to='profilepics')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user
class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=520)
    phone=models.IntegerField()
    pincode=models.IntegerField()
    land_mark=models.CharField(max_length=400)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=502)



import random
from django.utils import timezone
from datetime import timedelta

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()

    def is_valid(self):
        now = timezone.now()
        return now - self.created_at < timedelta(minutes=3)  # OTP is valid for 10 minutes

    