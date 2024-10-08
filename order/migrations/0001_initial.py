# Generated by Django 5.1.1 on 2024-09-22 10:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_alter_user_phone_number_and_more'),
        ('common', '0002_remove_region_code_alter_media_file_and_more'),
        ('product', '0002_productcolor_productimage_productreview_productsize_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=60)),
                ('max_limit_price', models.FloatField()),
                ('percertage', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Discount',
                'verbose_name_plural': 'Discounts',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('zip_code', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=120)),
                ('address', models.TextField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.region')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branchs',
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=120)),
                ('card_number', models.CharField(max_length=60)),
                ('expire_date', models.DateTimeField()),
                ('cvv', models.CharField(max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cart item',
                'verbose_name_plural': 'Cart items',
            },
        ),
        migrations.CreateModel(
            name='DeliveryTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('high', models.FloatField()),
                ('width', models.FloatField()),
                ('weight', models.FloatField()),
                ('price', models.FloatField()),
                ('delivary_time', models.TimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.branch')),
                ('regions', models.ManyToManyField(related_name='delivery_tariff', to='common.region')),
            ],
            options={
                'verbose_name': 'Delivery tariff',
                'verbose_name_plural': 'Delivery tariff',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('created', 'Created'), ('in_progress', 'In_progress'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'), ('finished', 'Finished')], max_length=60)),
                ('total_price', models.FloatField()),
                ('payment_status', models.CharField(choices=[('created', 'Created'), ('pending', 'Pending'), ('paid', 'Paid'), ('cancelled', 'Cancelled')], max_length=60)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('payme', 'Payme'), ('click', 'Click')], max_length=60)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='account.useraddress')),
                ('delivery_tariff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.deliverytariff')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.discount')),
                ('items', models.ManyToManyField(related_name='orders', to='order.cartitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
