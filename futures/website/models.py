from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=200)
  expires_at = models.DateField('expiration date')
  price = models.FloatField()

  def __str__(self):
    return self.name
