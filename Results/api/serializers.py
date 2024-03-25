from rest_framework import serializers
from Results.models import Results
from Scan.api.serializers import ScanSerializer

class ResultsSerializer(serializers.ModelSerializer):
    scan = ScanSerializer()
    class Meta:
        model = Results
        fields = '__all__'