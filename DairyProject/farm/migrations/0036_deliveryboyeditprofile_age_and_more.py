# Generated by Django 4.2.5 on 2024-03-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0035_remove_deliveryboy_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboyeditprofile',
            name='age',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='deliveryboyeditprofile',
            name='gender',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
