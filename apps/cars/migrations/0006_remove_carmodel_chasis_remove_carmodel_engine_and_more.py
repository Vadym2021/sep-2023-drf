# Generated by Django 5.0.5 on 2024-05-07 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carmodel_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='chasis',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='engine',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='price',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='seats',
        ),
    ]