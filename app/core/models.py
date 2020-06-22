import uuid
import datetime
import os
from urllib.request import urlopen
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from core.datalist import AllInfo
from django.core.files import File
from tempfile import NamedTemporaryFile


def product_image_path(instance, filename):
    """Generate file path"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/products/', filename)


def bill_payment_image(instance, filename):
    """Generate file path for bill"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/bill/', filename)


class UserManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, username, email, password=None):
        """Create new user profile"""
        if not username:
            raise ValueError('User must have a username')
        if not email:
            raise ValueError('User must have an email')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        """Create and save a new superuser with given details"""
        user = self.create_user(username, email, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        profile = Profile.objects.create(user_id=user.id)
        profile.save()

        cart = Cart.objects.create(user_id=user.id)
        cart.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name_plural = "User"


class Profile(models.Model):
    """ Profile model """
    SEX_TYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('LGBT', 'LGBT')
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    tel = models.CharField(max_length=12, blank=True)
    dob = models.DateField(auto_now=False, null=True)
    sex = models.CharField(
        max_length=10,
        choices=SEX_TYPE,
        blank=True
    )
    profile_status = models.BooleanField(default=False)

    def __str__(self):
        user = User.objects.get(pk=self.user_id)
        name = user.username
        return name

    class Meta:
        verbose_name_plural = "Profile"


class Address(models.Model):
    """ All address in the system"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    recipient = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    city = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)
    state = models.CharField(
        choices=AllInfo.CITY_NAME,
        max_length=30,
    )

    def __str__(self):
        user = User.objects.get(pk=self.user_id)
        name = user.username
        return name + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Address"


class Category(models.Model):
    type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Category"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, unique=False)
    pic1 = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    pic2 = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    pic3 = models.ImageField(upload_to=product_image_path, null=True, blank=True)
    url = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """ save data as url """
        if self.url and not self.pic1:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(self.url).read())
            img_temp.flush()
            self.pic1.save(f"image_{self.pk}.jpg", File(img_temp, 'rb'))
        super(Product, self).save(*args, **kwargs)

        class Meta:
            verbose_name_plural = "Product"


class Code(models.Model):
    """code table for adding code"""
    name = models.CharField(max_length=255)
    percent = models.DecimalField(max_digits=7, decimal_places=2)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Code"


class Cart(models.Model):
    """ Cart for each user """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    code = models.ForeignKey(
        Code,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    checkout_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Cart"


class CartDetail(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        carted = Cart.objects.get(pk=self.cart_id)
        return carted.user.username

    class Meta:
        verbose_name_plural = "Cart Detail"


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    address = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    shipping_fee = models.DecimalField(max_digits=7, decimal_places=2)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    payment_type = models.CharField(
        choices=AllInfo.PAYMENT_TYPE,
        max_length=50,
        blank=True,
        null=True
    )
    tracking_no = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    delivery_status = models.CharField(
        choices=AllInfo.DELIVER_TYPE,
        max_length=50,
        default=AllInfo.WAITING
    )
    code = models.CharField(max_length=255, blank=True, null=True)
    expected_arrive = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        user = User.objects.get(pk=self.user_id)
        name = user.username
        return name + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Order"


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        order = Order.objects.get(pk=self.order_id)
        product = Product.objects.get(pk=self.product_id)
        return product.title + " " + str(order.id)

    class Meta:
        verbose_name_plural = "Order Detail"

class PaymentBill(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    pic = models.ImageField(upload_to=bill_payment_image, null=True, blank=True)
    time_transfer = models.DateTimeField()
    approve_status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):
        """ change state of some order """
        if self.approve_status:
            order_data = self.order
            order_data.payment_status = True
            order_data.save()
        else:
            order_data = self.order
            order_data.payment_status = False
            order_data.save()
        super(PaymentBill, self).save(*args, **kwargs)

    def get_total_price(self):
        """ Get total price """
        order_price = self.order.total_price
        return order_price
    get_total_price.short_description = 'Total Price'

    class Meta:
        verbose_name_plural = "Payment Bill"


class ShippingRate(models.Model):
    """ The price for shipping """
    price = models.DecimalField(max_digits=7, decimal_places=2)
    post_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Shipping Rate"


class CarouselImage(models.Model):
    """Carousel Image"""
    picture = models.ImageField(upload_to=product_image_path, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Carousel Image"


class FooterData(models.Model):
    """Add data in footer"""
    phone = models.CharField(max_length=12, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Footer Data"


class Banner(models.Model):
    """Data for red banner"""
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Banner"


class NotifyEmail(models.Model):
    """Email to send notification to"""
    email = models.EmailField(max_length=255)

    class Meta:
        verbose_name_plural = "Notify Email"
