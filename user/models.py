from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
import importlib
# Create your models here.

class User(AbstractUser):
    koios_points = models.IntegerField(default = 0, help_text = 'number of koios points')
# Create your models here.
