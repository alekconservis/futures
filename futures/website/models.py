from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    cash_balance = models.FloatField(default=100.0)


class Product(models.Model):
    name = models.CharField(max_length=200)
    expires_at = models.DateField('expiration date')
    price = models.FloatField()

    def __str__(self):
        return self.name

