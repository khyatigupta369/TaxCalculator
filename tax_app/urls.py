from django.urls import path, include
from .views import FinancialYearList, TaxCalculator

# /tax_project/urls.py ---> /tax_app/urls.py
# financial-years - GET request
# tax-calculator - POST request
urlpatterns = [
    path('financial-years/', FinancialYearList.as_view(), name='financial-year-list'),
    path('tax-calculator/', TaxCalculator.as_view(), name='tax-calculator'),
]

