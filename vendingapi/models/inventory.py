from django.db import models

class Inventory(models.Model):
    """
    This makes an inventory instance and defines the columns in the DB

    """

    name = models.CharField(max_length=75, null=True)
    quantity = models.IntegerField(null=True)


    class Meta:
        verbose_name = ("inventory")
        verbose_name_plural = ("inventories")

    def __str__(self):
        return f'{self.name}'