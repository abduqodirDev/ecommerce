# Generated by Django 5.1.1 on 2024-09-20 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
                ('apartment', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User address',
                'verbose_name_plural': 'User addresses',
            },
        ),
        migrations.CreateModel(
            name='VerificationOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('type', models.CharField(choices=[('1', 'REGISTER'), ('2', 'RESET_PASSWORD')], max_length=1)),
                ('expires_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verification_otp', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Verification otp',
                'verbose_name_plural': 'Verification otps',
            },
        ),
    ]
