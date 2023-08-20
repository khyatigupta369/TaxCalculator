# # tax_app/views.py
# from rest_framework import generics, status
# from rest_framework.response import Response

# # Import Models and Serialisers
# from .models import TaxationScheme
# from .serializers import TaxationSchemeSerializer

# # Views
# class FinancialYearList():
#     queryset = TaxationScheme.objects.all()
#     serializer_class = TaxationSchemeSerializer

# class TaxCalculator(generics.CreateAPIView):
#     serializer_class = TaxationSchemeSerializer

#     def post(self, request, *args, **kwargs):
#         amount = request.data.get('amount')
#         year = request.data.get('year')
#         try:
#             taxation_scheme = TaxationScheme.objects.get(year=year)
#             tax = (taxation_scheme.tax_rate / 100) * amount
#             return Response({"tax_amount": tax}, status=status.HTTP_200_OK)
#         except TaxationScheme.DoesNotExist:
#             return Response({"error": "Taxation scheme not found for the specified year."}, status=status.HTTP_404_NOT_FOUND)


from django.shortcuts import render
from rest_framework import viewsets
from tax_app.models import TaxationScheme
from tax_app.serializers import TaxationSchemeSerializer

class taxViewSet(viewsets.ModelViewSet):
    queryset = TaxationScheme.objects.all()
    serializer_class = TaxationSchemeSerializer