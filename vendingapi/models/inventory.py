from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Inventory(models.Model):
    """
    This makes an inventory instance and defines the columns in the DB

    """
    name = models.CharField(max_length=75, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True) # Note: If there was a method to restock the machine, I would use some type of validator to make sure the quantity of beverages being put into the machine was not > 5

    class Meta:
        verbose_name = ("inventory")
        verbose_name_plural = ("inventories")
