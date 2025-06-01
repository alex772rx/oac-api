from rest_framework import viewsets
from .models import Sales
from .serializers import SalesSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
