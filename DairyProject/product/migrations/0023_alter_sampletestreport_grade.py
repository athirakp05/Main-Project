# Generated by Django 4.2.5 on 2024-04-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_remove_milkcollection_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampletestreport',
            name='grade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
