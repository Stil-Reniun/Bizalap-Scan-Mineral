from rest_framework.routers import DefaultRouter
from  Results.api.views import ResultsApiViewSet

router_result = DefaultRouter()
router_result.register(prefix='results', basename='results', viewset=ResultsApiViewSet)