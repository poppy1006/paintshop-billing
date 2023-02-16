# Generated by Django 4.0.6 on 2023-01-07 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_alter_bill_date_of_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sales_man',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField(max_length=15)),
            ],
        ),
    ]