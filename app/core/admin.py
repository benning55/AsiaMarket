from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Address)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Code)
admin.site.register(models.Cart)
admin.site.register(models.CartDetail)
admin.site.register(models.Order)
admin.site.register(models.OrderDetail)
