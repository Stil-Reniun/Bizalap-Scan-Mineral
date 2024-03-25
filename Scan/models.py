from django.core.validators import FileExtensionValidator
from django.db import models
from django.db.models import SET_NULL
from django.core.exceptions import ValidationError
from Users.models import User
from Upload.models import Upload

def validate_file_extension(value):
    if not value.name.endswith(('.pdf', '.csv')):
        raise ValidationError('Only PDF and CSV files are allowed.')

class Scan(models.Model):
    #details = models.FileField(upload_to='Scan/image/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'csv']), validate_file_extension])
    details = models.TextField(max_length=5)

    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    upload = models.ForeignKey(Upload, on_delete=SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.details