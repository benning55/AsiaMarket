import csv
import decimal

from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
import base64
# Register your models here.
from django.shortcuts import redirect
from django.urls import path
from weasyprint import HTML
import tempfile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from core import models
from core.models import OrderDetail
import datetime


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
    list_display = ['id', 'user', 'address', 'country', 'payment_type', 'payment_status', 'delivery_status', 'tracking_no', 'created']
    list_display_links = ['id', 'user']
    list_editable = ['delivery_status', 'tracking_no']
    list_filter = ['delivery_status', 'payment_type', ('created', DateFieldListFilter)]
    list_per_page = 10
    actions = ['set_delivery_to_shipping']

    ordering = ['-created']
    search_fields = ['user__username', 'id']

    inlines = [OrderDetailInLine]

    change_form_template = "pdf_admin.html"

    def set_delivery_to_shipping(self, request, queryset):
        queryset.update(delivery_status='Shipping')
    set_delivery_to_shipping.short_description = "Change selected waiting to shipping stage"

    def response_change(self, request, obj):
        if "_make-pdf" in request.POST:
            order_detail = OrderDetail.objects.all().filter(order_id=obj.id)
            special_address_check = models.SpecialAddress.objects.all().filter(pk=obj.id)
            address = special_address_check[0].address if len(special_address_check) > 0 else obj.address
            tax_16 = 0
            tax_5 = 0
            for products in order_detail:
                if 'Other' in products.product.category.type or 'Beverages' in products.product.category.type:
                    tax_16 += products.product.price
                else:
                    tax_5 += products.product.price
            tax_16 = decimal.Decimal(16/100) * tax_16
            tax_5 = decimal.Decimal(5/100) * tax_5
            total_tax = tax_16 + tax_5
            price_no_tax = obj.price - total_tax - obj.shipping_fee
            html_string = render_to_string('reciept/order_reciept.html', {
                'order_detail': order_detail,
                'order': obj,
                'address': address,
                'data': 'Hello Benning',
                'tax_16': "{:.2f}".format(float(tax_16)),
                'tax_5': "{:.2f}".format(float(tax_5)),
                'price_no_tax': "{:.2f}".format(float(price_no_tax))
            })
            html = HTML(string=html_string)
            result = html.write_pdf()

            # Creating http response
            response = HttpResponse(content_type='application/pdf;')
            response['Content-Disposition'] = f'attachment; filename=order_no{obj.id}.pdf'
            response['Content-Transfer-Encoding'] = 'binary'
            with tempfile.NamedTemporaryFile(delete=True) as output:
                output.write(result)
                output.flush()
                output = open(output.name, 'rb')
                response.write(output.read())
            return response
        else:
            return HttpResponseRedirect(request.path_info)


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
    list_display = ['id', 'username', 'first_name', 'last_name', 'age', 'is_active', 'is_staff']
    list_display_links = ['id', 'username']
    list_filter = ['is_staff', 'is_active']

    inlines = [ProfileDetailInLine, AddressDetailInLine]

    change_list_template = 'new_user_template.html'

    def has_add_permission(self, request):
        return False

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('new-csv/', self.look_user)
        ]
        return my_urls + urls

    def look_user(self, request):
        """get user list to csv"""
        all_user = models.User.objects.all()
        response = HttpResponse(content_type='text/csv')

        writer = csv.writer(response)
        writer.writerow(['Email', 'First Name', 'Last Name', 'Sex', 'DOB', 'Age', 'Tel'])

        for user in all_user:
            age = self.age(user)
            data = (user.email, user.first_name, user.last_name, user.profile.sex, user.profile.dob, age, user.profile.tel)
            writer.writerow(data)

        response['Content-Disposition'] = 'attachment; filename="user.csv"'
        return response

    def age(self, obj):
        user_id = obj.id
        profile = models.Profile.objects.get(pk=user_id)
        cur_date = datetime.datetime.now().date()
        dob = "None" if profile.dob is None else profile.dob
        if dob == "None":
            return dob
        else:
            age = (cur_date - dob).days // 365
            return age


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'tel', 'dob', 'sex']
    list_filter = ['sex']
    list_display_links = ['user']

    search_fields = ['user__username']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'country', 'city', 'post_code', 'state']
    list_display_links = ['id', 'user']
    list_filter = ['state']

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
    list_display = ['price', 'country']


class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'picture']


class FooterDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'email', 'address']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']


class NotifyEmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']


class UtilAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'value']


class SpecialAddressAdmin(admin.ModelAdmin):
    list_display = ['order', 'address']


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
admin.site.register(models.Util, UtilAdmin)
admin.site.register(models.SpecialAddress, SpecialAddressAdmin)