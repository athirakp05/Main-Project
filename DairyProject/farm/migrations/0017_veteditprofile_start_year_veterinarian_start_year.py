# Generated by Django 4.2.5 on 2024-02-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0016_remove_deliveryboy_user_alter_customuser_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veteditprofile',
            name='start_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='veterinarian',
            name='start_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]