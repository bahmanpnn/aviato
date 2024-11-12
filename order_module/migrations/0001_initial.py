# Generated by Django 5.0.7 on 2024-11-11 17:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_module', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('final_price', models.BigIntegerField(blank=True, null=True)),
                ('order_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail', to='order_module.orderbasket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product_module.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderSubmittedAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=127)),
                ('address', models.CharField(max_length=127)),
                ('zip_code', models.CharField(max_length=127)),
                ('city', models.CharField(max_length=127)),
                ('country', models.CharField(max_length=127)),
                ('order_basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_module.orderbasket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]