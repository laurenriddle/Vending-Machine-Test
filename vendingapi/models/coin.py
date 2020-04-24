from django.db import models

class Coin(models.Model):
    """
    This makes an inventory instance and defines the columns in the DB

    """

    coin = models.IntegerField(null=True)


    class Meta:
        verbose_name = ("coin")
        verbose_name_plural = ("coins")

    def __str__(self):
        return f'{self.coin}'