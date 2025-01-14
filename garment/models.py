from django.db import models

from accounts.models import Publisher

class Garment(models.Model):
    SIZE_CHOICES = [
        (1, 'Extra Small'),
        (2, 'Small'),
        (3, 'Medium'),
        (4, 'Large'),
        (5, 'Extra Large'),
    ]

    TYPE_CHOICES = [
        (1, 'Shirt'),
        (2, 'Pants')
    ]

    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='garments')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.PositiveSmallIntegerField(choices=SIZE_CHOICES)
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)

    class Meta:
        db_table = 'garment'

    def __str__(self):
        return f"{self.type} ({self.size}) - {self.price}"
