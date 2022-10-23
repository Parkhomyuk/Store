# Generated by Django 4.1.1 on 2022-10-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_title_parentcharacteristic_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='characteristic',
        ),
        migrations.AddField(
            model_name='characteristic',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='parentCharacteristic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.parentcharacteristictype'),
        ),
    ]
