# Generated by Django 2.2.9 on 2020-01-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, choices=[('Baden-Württemberg', 'Baden-Württemberg'), ('Bayern', 'Bayern'), ('Berlin', 'Berlin'), ('Brandenburg', 'Brandenburg'), ('Bremen', 'Bremen'), ('Hamburg', 'Hamburg'), ('Hessen', 'Hessen'), ('Niedersachsen', 'Niedersachsen'), ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'), ('Nordrhein-Westfalen', 'Nordrhein-Westfalen'), ('Rheinland-Pfalz', 'Rheinland-Pfalz'), ('Saarland', 'Saarland'), ('Sachsen', 'Sachsen'), ('Sachsen-Anhalt', 'Sachsen-Anhalt'), ('Schleswig-Holstein', 'Schleswig-Holstein'), ('Thüringen', 'Thüringen')], max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='house_number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='recipient',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
