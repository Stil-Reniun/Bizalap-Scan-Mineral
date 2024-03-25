from rest_framework.routers import DefaultRouter
from Scan.api.views import  SampleApiViewSet

router_scan = DefaultRouter()
router_scan.register(prefix='scan', basename='scan', viewset=SampleApiViewSet)