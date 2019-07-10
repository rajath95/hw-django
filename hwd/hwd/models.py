from django.db import models
from djmoney.models.fields import MoneyField


class Books(models.Model):



    title=models.CharField(max_length=30)

    author=models.CharField(max_length=30)

    price=MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=11,
    )

    def __str__(self):
        return self.title
