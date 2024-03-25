from django.db import models
from django.db.models import SET_NULL
from django.core.exceptions import ValidationError
from Users.models import User

def validate_image_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Formato de archivo no admitido. Solo se permiten archivos JPG, PNG o JPEG.'))

class Upload(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Upload/Images/', validators=[validate_image_extension])
    microscope_analyzer = models.SlugField(max_length=10)
    number_samples = models.IntegerField()
    number_capa = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    def __str__(self):
        return self.title