from rest_framework import serializers
from Upload.models import Upload
from Users.api.serializers import UserDetailSerializer

class UploadSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = Upload
        fields = '__all__'