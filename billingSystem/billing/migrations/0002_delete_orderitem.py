# Generated by Django 5.0.4 on 2024-04-10 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
