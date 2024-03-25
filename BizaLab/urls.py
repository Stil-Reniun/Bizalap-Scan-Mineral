from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="BizaLab Scan Mineral",
        default_version='v0.1',
        description="BizaLab Scan Mineral es una API REST FULL diseñada para el escaneo de minerales a base de imagenes microscopicas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ash_vi@hotmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('Users.api.routers')),
]
