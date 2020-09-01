
from django.core.management.base import BaseCommand, CommandError

from core.models import Product, NotifyEmail, Address


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    # @periodic_task(run_every=crontab(minute=1))
    def handle(self, *args, **options):
        all_address = Address.objects.all()
        for address in all_address:
            if len(address.recipient.split()) == 1:
                address.recipient = address.user.first_name + " " + address.user.last_name
                address.save()
