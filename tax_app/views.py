from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from tax_app.models import TaxationScheme

class TaxViewSet(viewsets.ModelViewSet):
    queryset = TaxationScheme.objects.all()
    serializer_class = TaxSerializer