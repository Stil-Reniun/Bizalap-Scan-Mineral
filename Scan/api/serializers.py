from rest_framework import serializers
from Scan.models import Scan
from Users.api.serializers import UserDetailSerializer
from Upload.api.serializers import UploadSerializer

class ScanSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    upload = UploadSerializer()
    class Meta:
        model = Scan
        fields = '__all__'