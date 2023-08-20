# Import necessary modules
from rest_framework import generics, status
from rest_framework.response import Response

# Import models and serializers
from .models import TaxationScheme
from .serializers import TaxationSchemeSerializer

# Define views
class FinancialYearList(generics.ListAPIView):
    queryset = TaxationScheme.objects.all()
    serializer_class = TaxationSchemeSerializer

class TaxCalculator(generics.CreateAPIView):
    serializer_class = TaxationSchemeSerializer

    def post(self, request):
        print("Request data:", request.data)
        amount = float(request.data.get('amount'))
        year = request.data.get('year')
        print("Amount:", amount)
        print("Year:", year)
        try:
            taxation_scheme = TaxationScheme.objects.get(year=year)
            print("Taxation Scheme:", taxation_scheme)
            tax = (taxation_scheme.tax_rate * amount)/100
            return Response({"tax_amount": tax}, status=status.HTTP_200_OK)
        except TaxationScheme.DoesNotExist:
            return Response({"error": "Taxation scheme not found for the specified year."}, status=status.HTTP_404_NOT_FOUND)
