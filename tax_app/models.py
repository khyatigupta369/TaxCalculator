# tax_app/models.py
from django.db import models

class TaxationScheme(models.Model):
    year = models.PositiveIntegerField(unique=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"TaxationScheme - {self.year}"
