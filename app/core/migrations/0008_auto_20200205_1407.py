# Generated by Django 2.2.9 on 2020-02-05 14:07

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200205_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.product_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.product_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.product_image_path),
        ),
    ]