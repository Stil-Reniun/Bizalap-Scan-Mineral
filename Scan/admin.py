from django.contrib import admin
from Scan.models import Scan

@admin.register(Scan)
class BooksAdmin(admin.ModelAdmin):
    pass