# Generated by Django 3.0.7 on 2021-08-23 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dentist', '0006_auto_20210820_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='patient',
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
