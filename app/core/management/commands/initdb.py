from abc import ABC

from django.core.management import BaseCommand, CommandError

from core.models import Category, User, Product


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
            Category.objects.create(type='Fruits and Vegetables', color='green').save()
            Category.objects.create(type='Dry goods and Seasonings', color='blue').save()
            Category.objects.create(type='Rice Flour and Noodles', color='yellow').save()
            Category.objects.create(type='Condiments and Sauces', color='red').save()
            Category.objects.create(type='Normal and Alcoholic Beverages', color='black').save()
            Category.objects.create(type='Snack', color='orange').save()
            Category.objects.create(type='Frozen Products', color='purple').save()
            Category.objects.create(type='Other', color='pink').save()
        else:
            self.stdout.write("Category Data already add.")

        product = Product.objects.all()
        if product.count() < 1:
            Product.objects.create(
                category_id=1,
                title="test",
                pic1="",
                pic2="",
                pic3="",
                url="https://lh3.googleusercontent.com/proxy/LSCAnu-GvPBTKR568Eo-fzoLqXBof8p-q_RCwDVQxD8BsbyMZLbIuU7HA2vuw1UdV9s9KdBBLsX2kmQcoWv_G-mtM6KmAqnPgJrOB_qQYToxFSXfbKItQPgBaK9KsBGwFo4",
                description="Thai food defult",
                price=25,
                quantity=10
            ).save()
        else:
            self.stdout.write("Product was made")
