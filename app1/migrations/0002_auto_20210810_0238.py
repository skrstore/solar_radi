# Generated by Django 2.2.5 on 2021-08-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction1',
            name='Fuel_Type',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='prediction1',
            name='Name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='prediction1',
            name='Owner_Type',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='prediction1',
            name='Transmission',
            field=models.CharField(max_length=5),
        ),
    ]
