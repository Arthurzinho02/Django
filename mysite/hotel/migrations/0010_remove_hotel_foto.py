# Generated by Django 5.0.5 on 2024-05-16 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_hotel_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='foto',
        ),
    ]