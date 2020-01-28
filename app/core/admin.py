from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Address)
