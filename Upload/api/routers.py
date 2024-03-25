from rest_framework.routers import DefaultRouter
from Upload.api.views import UploadApiViewSet

router_upload = DefaultRouter()
router_upload.register(prefix='upload', basename='upload', viewset=UploadApiViewSet)