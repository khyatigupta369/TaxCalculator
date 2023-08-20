from django.urls import path, include
from tax_app.views import taxViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
router.register(r'taxScheme', taxViewSet)


urlpatterns = [
    path('', include(routers.urls))
]
