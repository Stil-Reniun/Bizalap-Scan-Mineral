from rest_framework.viewsets import ModelViewSet
from Scan.models import Scan
from django_filters.rest_framework import DjangoFilterBackend
from  Scan.api.serializers import ScanSerializer
from Scan.api.permissions import IsAdminOrReadOnly

class SampleApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ScanSerializer
    queryset = Scan.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
