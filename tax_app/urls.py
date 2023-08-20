from django.urls import path, include
from tax_app.views import taxViewSet
from rest_framework import routers

# routers = routers.DefaultRouter()
# routers.register(r'taxScheme', taxViewSet)


# urlpatterns = [
#     path('', include(routers.urls))
# ]

# tax_app/urls.py
from django.urls import path
from .views import FinancialYearList, TaxCalculator

urlpatterns = [
    path('financial-years/', FinancialYearList.as_view(), name='financial-year-list'),
    path('tax-calculator/', TaxCalculator.as_view(), name='tax-calculator'),
]

