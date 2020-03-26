from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
import base64
# Register your models here.
from django.shortcuts import redirect
from weasyprint import HTML
import tempfile
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from core import models
from core.models import OrderDetail


class OrderInLine(admin.TabularInline):
    model = models.Order
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False


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
    list_filter = ['delivery_status', 'payment_type', ('created', DateFieldListFilter)]
    list_per_page = 10
    actions = ['set_delivery_to_shipping']

    ordering = ['-created']
    search_fields = ['user__username']

    inlines = [OrderDetailInLine]

    change_form_template = "pdf_admin.html"

    def set_delivery_to_shipping(self, request, queryset):
        queryset.update(delivery_status='Shipping')
    set_delivery_to_shipping.short_description = "Change selected waiting to shipping stage"

    def response_change(self, request, obj):
        if "_make-pdf" in request.POST:
            order_detail = OrderDetail.objects.all().filter(order_id=obj.id)
            html_string = render_to_string('reciept/order_reciept.html', {
                'order_detail': order_detail,
                'order': obj,
                'data': 'Hello Benning'
            })
            html = HTML(string=html_string)
            result = html.write_pdf()

            # Creating http response
            response = HttpResponse(content_type='application/pdf;')
            response['Content-Disposition'] = 'inline; filename=test.pdf'
            response['Content-Transfer-Encoding'] = 'binary'
            with tempfile.NamedTemporaryFile(delete=True) as output:
                output.write(result)
                output.flush()
                output = open(output.name, 'rb')
                response.write(output.read())
            return response


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

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions


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


class PaymentBillAdmin(admin.ModelAdmin):
    list_display = ['order', 'get_total_price', 'pic', 'time_transfer', 'approve_status', 'created']
    list_editable = ['approve_status']
    list_filter = ['approve_status', ('created', DateFieldListFilter)]

    ordering = ['-created']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity']


class ShippingRateAdmin(admin.ModelAdmin):
    list_display = ['price', 'post_code']


class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture']


class FooterDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'email', 'address']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']


class NotifyEmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Code, CodeAdmin)
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.CartDetail, CartDetailAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderDetail, OrderDetailAdmin)
admin.site.register(models.PaymentBill, PaymentBillAdmin)
admin.site.register(models.ShippingRate, ShippingRateAdmin)
admin.site.register(models.CarouselImage, CarouselImageAdmin)
admin.site.register(models.FooterData, FooterDataAdmin)
admin.site.register(models.Banner, BannerAdmin)
admin.site.register(models.NotifyEmail, NotifyEmailAdmin)
