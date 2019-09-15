import email
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    is_worthy = models.BooleanField(default=None, blank=True, null=True)


