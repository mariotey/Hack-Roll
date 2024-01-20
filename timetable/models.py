from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    user_image = models.TextField(blank=True)
