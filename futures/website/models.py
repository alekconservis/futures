import random
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)
    cash_balance = models.FloatField(default=100.0)


# Create your models here.
class Product(models.Model):
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    unit = models.CharField(max_length=25, default='unit(s)')
    default_quantity = models.IntegerField('quantity', default=1)

    def __str__(self):
        return self.name

    def fluctuate(self):
        # set PRICE to random value within certain range of original value
        offset = random.randrange(-50, 50, 1)
        self.price = self.price + round(Decimal(offset / 100), 2)
        self.save()


class Contract(models.Model):
    created_at = models.DateTimeField(default=now, blank=True)
    updated_at = models.DateTimeField(default=now, blank=True)
    seller = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='sell_contracts')
    buyer = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='buy_contracts')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.CharField(max_length=255)
    end_date = models.DateField('maturity date')

    def purchase_action(self):
        if self.buyer is None:
            return 'Buy From Contract'
        else:
            return 'Sell To Contract'
