# Generated by Django 4.1.1 on 2022-10-18 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_catalog_0_catalog_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.catalog_1'),
            preserve_default=False,
        ),
    ]