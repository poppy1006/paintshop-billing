# Generated by Django 4.0.6 on 2023-01-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0008_alter_bill_date_of_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='item_name',
            field=models.TextField(max_length=5000),
        ),
    ]
