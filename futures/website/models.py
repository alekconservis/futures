from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    cash_balance = models.FloatField(default=100.0)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    expires_at = models.DateField('expiration date')
    price = models.FloatField()

    def __str__(self):
        return self.name


class Contract(models.Model):
    seller = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='sell_contracts')
    buyer = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='buy_contracts')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.CharField(max_length=255)
    end_date = models.DateField()
