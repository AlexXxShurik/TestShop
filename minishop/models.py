from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.ForeignKey(
        'Currency',
        related_name='cur',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Currency(models.Model):
    currency = models.CharField(max_length=255, blank=True, null=True)
    name_web = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.currency

    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюта'


