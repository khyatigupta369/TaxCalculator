# tax_app/admin.py
from django.contrib import admin
from .models import TaxationScheme

# built-in portal registeration
admin.site.register(TaxationScheme)
