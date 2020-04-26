from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Inventory(models.Model):
    """
    This makes an inventory instance and defines the columns in the DB

    """
    name = models.CharField(max_length=75, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)

    class Meta:
        verbose_name = ("inventory")
        verbose_name_plural = ("inventories")
