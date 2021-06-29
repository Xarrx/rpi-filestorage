from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ImageData)
admin.site.register(models.ThumbnailData)
admin.site.register(models.ImageTag)
admin.site.register(models.ImageTagAssoc)
