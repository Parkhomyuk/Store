# Generated by Django 4.1.1 on 2022-10-24 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_rename_create_by_product_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priceproduct',
            name='product',
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
