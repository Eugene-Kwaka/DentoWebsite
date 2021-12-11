# Generated by Django 3.0.7 on 2021-08-20 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100, null=True)),
                ('contact_email', models.EmailField(max_length=254, null=True)),
                ('contact_message', models.TextField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('pic', models.ImageField(blank=True, default='s9.png', null=True, upload_to='img')),
                ('stage', models.IntegerField(null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('schedule', models.CharField(choices=[('9 AM to 10 AM', '9 AM to 10 AM'), ('10 AM to 11 AM', '10 AM to 11 AM'), ('11 AM to 12 PM', '9 AM to 12 PM'), ('2 PM to 3 PM', '2 PM to 3 PM')], max_length=50, null=True)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=50, null=True)),
                ('message', models.TextField(max_length=200, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dentist.Patient')),
            ],
        ),
    ]
