# Generated by Django 2.2.9 on 2020-01-27 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200125_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(choices=[('Baden-Württemberg', 'Baden-Württemberg'), ('Bayern', 'Bayern'), ('Berlin', 'Berlin'), ('Brandenburg', 'Brandenburg'), ('Bremen', 'Bremen'), ('Hamburg', 'Hamburg'), ('Hessen', 'Hessen'), ('Niedersachsen', 'Niedersachsen'), ('Mecklenburg-Vorpommern', 'Mecklenburg-Vorpommern'), ('Nordrhein-Westfalen', 'Nordrhein-Westfalen'), ('Rheinland-Pfalz', 'Rheinland-Pfalz'), ('Saarland', 'Saarland'), ('Sachsen', 'Sachsen'), ('Sachsen-Anhalt', 'Sachsen-Anhalt'), ('Schleswig-Holstein', 'Schleswig-Holstein'), ('Thüringen', 'Thüringen')], max_length=30),
        ),
        migrations.AlterField(
            model_name='address',
            name='house_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='post_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='recipient',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=255),
        ),
    ]
