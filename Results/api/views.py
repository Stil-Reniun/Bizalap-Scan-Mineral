from rest_framework.viewsets import ModelViewSet
from Results.api.serializers import ResultsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from Scan.api.permissions import IsAdminOrReadOnly

class ResultsApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = ResultsSerializer
    filter_backends = [DjangoFilterBackend]
