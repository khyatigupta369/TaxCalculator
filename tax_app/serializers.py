# tax_app/serializers.py
from rest_framework import serializers
from .models import TaxationScheme

# JSON parsing
class TaxationSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxationScheme
        fields = '__all__'
