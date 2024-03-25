from django.contrib import admin
from Results.models import Results

@admin.register(Results)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['id','details']
