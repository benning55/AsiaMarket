from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from core.datalist import AllInfo
from app.settings import MEDIA_ROOT


def product_image_path(instance, filename):
    """Generate file path"""
    return os.path.join('media', filename)


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


class Address(models.Model):
    """ All address in the system"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    recipient = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)
    city = models.CharField(
        choices=AllInfo.CITY_NAME,
        max_length=30,
    )

    def __str__(self):
        user = User.objects.get(pk=self.user_id)
        name = user.username
        return name


class Category(models.Model):
    type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    pic1 = models.ImageField(upload_to=product_image_path, null=True)
    pic2 = models.ImageField(upload_to=product_image_path, null=True)
    pic3 = models.ImageField(upload_to=product_image_path, null=True)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title

