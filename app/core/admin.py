from django.contrib import admin

# Register your models here.
from core import models


class OrderDetailInLine(admin.TabularInline):
    model = models.OrderDetail
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class ProfileDetailInLine(admin.TabularInline):
    model = models.Profile
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class CartDetailInLine(admin.TabularInline):
    model = models.CartDetail
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


class AddressDetailInLine(admin.TabularInline):
    model = models.Address
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


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'description', 'price', 'quantity']
    list_display_links = ['title']
    list_editable = ['quantity']
    list_filter = ['category']
    list_per_page = 20

    search_fields = ['title']


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff']
    list_display_links = ['id', 'username']
    list_filter = ['is_staff', 'is_active']

    inlines = [ProfileDetailInLine, AddressDetailInLine]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'tel', 'dob', 'sex']
    list_filter = ['sex']
    list_display_links = ['user']

    search_fields = ['user__username']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'street', 'house_number', 'post_code', 'city']
    list_display_links = ['id', 'user']
    list_filter = ['city']

    search_fields = ['user__username']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'color']
    list_display_links = ['id', 'type']

    search_fields = ['type']


class CartDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity', 'price']
    list_display_links = ['id', 'cart']

    search_fields = ['cart__user__username']


class CodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percent', 'start_date', 'end_date', 'quantity']
    list_display_links = ['id', 'name']
    list_editable = ['quantity']
    list_filter = ['percent']

    search_fields = ['name']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Code, CodeAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartDetail, CartDetailAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderDetail)
