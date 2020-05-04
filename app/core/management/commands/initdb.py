from abc import ABC

from django.core.management import BaseCommand, CommandError

from core.models import Category, User, Product, Banner
from django.contrib.auth.models import Group


class Command(BaseCommand):
    """Django command to add data to db"""

    def handle(self, *args, **options):
        admin, _ = Group.objects.get_or_create(name='admin')
        customer, _ = Group.objects.get_or_create(name='customer')
        users = User.objects.all()
        if users.count() < 1:
            self.stdout.write("Create super user")
            User.objects.create_superuser(
                username='admin',
                email='60070109@gmail.com',
                password='admin@kmitl'
            ).save()
        else:
            self.stdout.write("Already have super user")
        x = Category.objects.all()
        if x.count() < 1:
            self.stdout.write("Adding Category data to db")
            Category.objects.create(type='Fruits and Vegetables | ผักและผลไม้', color='green').save()
            Category.objects.create(type='Dry goods and Seasonings | ของแห้งและเครื่องปรุงรส', color='blue').save()
            Category.objects.create(type='Rice Flour and Noodles | แป้งและเส้น', color='yellow').save()
            Category.objects.create(type='Condiments and Sauces | เครื่องปรุงและซอส', color='red').save()
            Category.objects.create(type='Normal and Alcoholic Beverages | เครื่องดื่มและแอลกฮอล์', color='black').save()
            Category.objects.create(type='Snack | ขนมขบเคี้ยว', color='orange').save()
            Category.objects.create(type='Frozen Products | อาหารแช่แข็ง', color='purple').save()
            Category.objects.create(type='Other | อื่นๆ', color='pink').save()
        else:
            self.stdout.write("Category Data already add.")
        banner = Banner.objects.all()
        if banner.count() < 1:
            self.stdout.write("add banner example")
            Banner.objects.create(description='Example')
        else:
            pass
