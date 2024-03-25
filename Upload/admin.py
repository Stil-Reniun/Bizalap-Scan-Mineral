from django.contrib import admin
from Upload.models import Upload

@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['title', 'microscope_analyzer','number_samples','number_capa','created_at', 'user']
    #class Meta:
    #verbose_name_plural = "Muestras"