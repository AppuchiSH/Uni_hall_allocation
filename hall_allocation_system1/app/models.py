"""
Definition of models.
"""

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class PendingUser(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Store hashed in real-world cases
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com") 
    position = models.CharField(max_length=50)
    club_name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    lab = models.CharField(max_length=100, blank=True, null=True)

class ClubHead(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com")
    club = models.CharField(max_length=100)
    

class HOD(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com")
    department = models.CharField(max_length=100)

class FacultyInCharge(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com")
    department = models.CharField(max_length=100)

class ResourceApprovalPerson(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com")
    lab = models.CharField(max_length=100)

class Principal(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com")
    password = models.CharField(max_length=255)

class IQAC(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com")
class DeanOfStudentAffairs(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default="default_email@example.com")

    from django.db import models

class HallRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    applicant = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    purpose = models.TextField()
    podium = models.IntegerField(default=0)
    mic = models.IntegerField(default=0)
    led = models.IntegerField(default=0)
    stage = models.IntegerField(default=0)
    dias = models.IntegerField(default=0)
    participants = models.IntegerField()
    suggested_hall = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    rejection_reason = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.applicant} - {self.date} - {self.status}"



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
