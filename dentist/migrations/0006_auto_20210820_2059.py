# Generated by Django 3.0.7 on 2021-08-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0005_auto_20210820_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
