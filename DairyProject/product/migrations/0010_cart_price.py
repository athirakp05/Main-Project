# Generated by Django 4.2.5 on 2024-02-23 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_rename_antibiotic_residue_sampletestreport_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.FloatField(default=True),
        ),
    ]
