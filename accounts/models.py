from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    #이메일 사용하고 싶지 않을때 
    REQUIRED_FIELDS = []
    email = None
    
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

