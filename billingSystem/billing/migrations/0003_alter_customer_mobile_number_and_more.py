# Generated by Django 5.0.4 on 2024-04-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_delete_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
