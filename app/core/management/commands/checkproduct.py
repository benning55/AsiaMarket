from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
import time
import schedule
from django.template.loader import render_to_string

from core.models import Product


def check_product():
    queryset = Product.objects.all().filter(quantity__lte=10)
    if len(queryset) > 0:
        message = render_to_string('notify_product.html', {
            'queryset': queryset
        })
        send_mail(
            'Product is running out!',
            message,
            'no-reply@thaimarket.express',
            ['bmaisonti@gmail.com'],
            html_message=message,
            fail_silently=False
        )


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    # @periodic_task(run_every=crontab(minute=1))
    def handle(self, *args, **options):
        schedule.every(1).hours.do(check_product)

        while 1:
            schedule.run_pending()
            time.sleep(1)

