"""
Definition of models.
"""

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    designation = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Adding related_name to avoid reverse accessor clash
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Custom related name
        blank=True,
    )
