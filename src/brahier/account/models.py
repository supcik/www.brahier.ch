from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=32, blank=True)
    location = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    mobile_number = models.CharField(max_length=255, blank=True)
    registration_challenge = models.CharField(max_length=100, blank=True)