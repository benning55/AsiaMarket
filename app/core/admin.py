from django.contrib import admin

# Register your models here.
from core import models


class OrderDetailInLine(admin.TabularInline):
    model = models.OrderDetail
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class CartDetailInLine(admin.TabularInline):
    model = models.CartDetail
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'payment_type', 'payment_status', 'delivery_status', 'created']
    list_display_links = ['id', 'user']
    list_editable = ['delivery_status']
    list_filter = ['delivery_status', 'payment_type']
    list_per_page = 10
    actions = ['set_delivery_to_shipping']

    ordering = ['-created']
    search_fields = ['user__username']

    inlines = [OrderDetailInLine]

    def set_delivery_to_shipping(self, request, queryset):
        queryset.update(delivery_status='Shipping')
    set_delivery_to_shipping.short_description = "Change selected waiting to shipping stage"


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'code', 'checkout_status']
    list_display_links = ['user']
    list_filter = ['checkout_status']
    list_per_page = 10

    search_fields = ['user__username']

    inlines = [CartDetailInLine]


admin.site.register(models.User)
admin.site.register(models.Profile)
admin.site.register(models.Address)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.Code)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartDetail)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderDetail)
