from django.db import models

# Create your models here.
class Contract(models.Model):
    # seller = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    # buyer = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.CharField(max_length=255)
    end_date = models.DateField()
