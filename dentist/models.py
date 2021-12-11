from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your models here.


User = get_user_model()


# class Patient(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, null=True)
#     comment = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name


class Appointment(models.Model):
    SCHEDULES = (
        ('9 AM to 10 AM', '9 AM to 10 AM'),
        ('10 AM to 11 AM', '10 AM to 11 AM'),
        ('11 AM to 12 PM', '9 AM to 12 PM'),
        ('2 PM to 3 PM', '2 PM to 3 PM'),
    )

    DAYS = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
    )

    #patient_name = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    schedule = models.CharField(max_length=50, null=True, choices=SCHEDULES)
    day = models.CharField(max_length=50, null=True, choices=DAYS)
    message = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    pic = models.ImageField()
    stage = models.IntegerField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    contact_name = models.CharField(max_length=100, null=True)
    contact_email = models.EmailField(null=True)
    contact_message = models.CharField(max_length=200, null=True)
