# Generated by Django 5.0.4 on 2024-04-30 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='price',
            new_name='seats',
        ),
        migrations.AddField(
            model_name='carmodel',
            name='chasis',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='carmodel',
            table='cars',
        ),
    ]