from django.db import models
from django.db.models import SET_NULL
from Scan.models import Scan


class Results(models.Model):
    scan = models.ForeignKey(Scan, on_delete=SET_NULL, null=True)

    def details(self):
        if self.scan:
            return self.scan.details
        return None
