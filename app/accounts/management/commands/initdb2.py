from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User
from django.conf import settings


class Command(BaseCommand):
    help = 'Initialize database'

    def add_arguments(self, parser):
        parser.add_argument('project', type=str, nargs='?')

    def handle(self, *args, **options):
        self.initdb_standard()
        self.stdout.write(self.style.SUCCESS('Successfully initialized database'))

    def initdb_standard(self):
        self.stdout.write(self.style.NOTICE('initialize users ...'))

        admin, _ = Group.objects.get_or_create(name='Admin')
        customer, _ = Group.objects.get_or_create(name='Customer')

        # superuser, for accessing django admin page.
        sys_admin, sys_admin_created = User.objects.get_or_create(username='adminkmitl')
        if sys_admin_created:
            self.stdout.write(self.style.NOTICE('setup superuser ...'))
            sys_admin.set_password('benning55')
            sys_admin.is_superuser = True
            sys_admin.is_staff = True
            sys_admin.groups.add(admin)
            sys_admin.save()
