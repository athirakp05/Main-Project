# Generated by Django 4.2.5 on 2024-03-29 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0033_deliveryboy_is_approved_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryboyeditprofile',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='sellereditprofile',
            name='is_active',
        ),
    ]
