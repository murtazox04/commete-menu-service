# Generated by Django 5.0.6 on 2024-07-01 05:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'discounts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('price', models.FloatField()),
                ('discounted_price', models.FloatField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'dishes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DishParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dish_parameters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'db_table': 'menus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=255)),
            ],
            options={
                'db_table': 'parameters',
                'managed': False,
            },
        ),
    ]
