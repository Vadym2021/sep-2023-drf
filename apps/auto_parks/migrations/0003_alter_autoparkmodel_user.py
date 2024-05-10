# Generated by Django 5.0.5 on 2024-05-10 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0002_autoparkmodel_user'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoparkmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_parks', to='users.usermodel'),
        ),
    ]
