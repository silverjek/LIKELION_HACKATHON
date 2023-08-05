# Generated by Django 4.2 on 2023-08-05 09:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medi_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patName', models.CharField(max_length=30)),
                ('patSex', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=6)),
                ('patBirth', models.DateField()),
                ('patAddress', models.CharField(max_length=100)),
                ('patSSN', models.CharField(max_length=14)),
                ('patBlood', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('O', 'o'), ('AB', 'AB')], max_length=2)),
                ('patRH', models.CharField(choices=[('PLUS', '+'), ('MINUS', '-')], max_length=5)),
                ('patHeight', models.FloatField()),
                ('patWeight', models.FloatField()),
                ('patPhone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('updateDate', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Caution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cauLevel', models.CharField(choices=[('SEVERE', 'Severe'), ('MODERATE', 'Moderate'), ('MILD', 'Mild')], max_length=10)),
                ('cauName', models.CharField(max_length=300)),
                ('cauType', models.CharField(max_length=300)),
                ('cauSymptom', models.CharField(max_length=300)),
                ('info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.medi_info')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
