from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    portfolio_site = models.URLField(blank = True)
    
    def __str__(self):
        return self.user.username

class Trainee(models.Model):
    id = models.BigIntegerField(unique = True)
    address = models.TextField()
    city = models.TextField()
    crmid = models.TextField()
    description = models.TextField()
    name = models.TextField()
    website = models.TextField()
    logoUrl = models.TextField()
    noOfEmployees = models.TextField(default = None)
    sector = models.TextField(default = None)

    def __str__(self):
        return self.id