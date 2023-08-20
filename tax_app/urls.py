from django.urls import path, include
from .views import FinancialYearList, TaxCalculator

urlpatterns = [
    path('financial-years/', FinancialYearList.as_view(), name='financial-year-list'),
    path('tax-calculator/', TaxCalculator.as_view(), name='tax-calculator'),
]

