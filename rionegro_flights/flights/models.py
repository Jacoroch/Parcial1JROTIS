from django.db import models

class Flight(models.Model):
    NATIONAL = 'Nacional'
    INTERNATIONAL = 'Internacional'

    TYPE_CHOICES = [
        (NATIONAL, 'Nacional'),
        (INTERNATIONAL, 'Internacional'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
