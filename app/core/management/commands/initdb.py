from abc import ABC

from django.core.management import BaseCommand, CommandError

from core.models import Category, User


class Command(BaseCommand):
    """Django command to add data to db"""

    def handle(self, *args, **options):
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
            Category.objects.create(type='Fruits and Vegetables', color='black').save()
            Category.objects.create(type='Dry goods and Seasonings', color='blue').save()
            Category.objects.create(type='Rice Flour and Noodles', color='yellow').save()
        else:
            self.stdout.write("Category Data already add.")
