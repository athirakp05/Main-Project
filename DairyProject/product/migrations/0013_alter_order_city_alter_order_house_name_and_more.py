# Generated by Django 4.2.5 on 2024-03-30 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_payment_payment_method_remove_payment_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='house_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='pin_code',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
