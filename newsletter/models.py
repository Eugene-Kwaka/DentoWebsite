from django.db import models

# Create your models here.


class Signup(models.Model):
    nl_email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
