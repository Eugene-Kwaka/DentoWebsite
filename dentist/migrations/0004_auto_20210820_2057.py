# Generated by Django 3.0.7 on 2021-08-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0003_auto_20210820_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
