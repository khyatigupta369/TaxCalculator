# tax_app/models.py
from django.db import models

# schema for the database
class TaxationScheme(models.Model):
    # year - unique positive inter field, and taxRate - decimal
    year = models.PositiveIntegerField(unique=True)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        # format for the string will be TaxationScheme - 2023
        return f"TaxationScheme - {self.year}"
