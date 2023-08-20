# tax_app/serializers.py
from rest_framework import serializers
from .models import TaxationScheme

class TaxationSchemeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaxationScheme
        fields = '__all__'
