# Generated by Django 2.2.10 on 2020-02-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200218_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(),
        ),
    ]