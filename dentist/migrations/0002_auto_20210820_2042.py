# Generated by Django 3.0.7 on 2021-08-20 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='pic',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
