# Generated by Django 5.0.5 on 2024-05-16 15:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
