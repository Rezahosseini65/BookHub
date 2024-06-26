# Generated by Django 5.0.4 on 2024-05-29 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='SKU')),
                ('buy_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='buy price')),
                ('sale_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='sale price')),
                ('num_stock', models.PositiveIntegerField(default=0, verbose_name='num stock')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stockrecords', to='books.book', verbose_name='stock record')),
            ],
        ),
    ]
