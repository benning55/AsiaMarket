# Generated by Django 2.2.10 on 2020-02-15 00:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('payment_status', models.BooleanField(default=False)),
                ('delivery_status', models.CharField(choices=[('W', 'Waiting for delivery'), ('S', 'In the process of shipping'), ('D', 'Delivered')], default='W', max_length=50)),
                ('expected_arrive', models.DateField(blank=True, null=True)),
                ('created', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Product')),
            ],
        ),
    ]
