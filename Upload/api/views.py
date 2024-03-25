from rest_framework.viewsets import ModelViewSet
from Upload.models import Upload
from django_filters.rest_framework import DjangoFilterBackend
from Upload.api.serializers import UploadSerializer
from Upload.api.permissions import IsAdminOrReadOnly

class UploadApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = UploadSerializer
    queryset = Upload.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
