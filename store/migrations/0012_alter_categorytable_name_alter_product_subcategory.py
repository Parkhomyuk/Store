# Generated by Django 4.1.1 on 2022-10-20 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_categoryplacetable_childid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytable',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categorytable'),
        ),
    ]
