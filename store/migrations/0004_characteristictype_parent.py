# Generated by Django 4.1.1 on 2022-10-06 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_title_parentcharacteristictype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristictype',
            name='parent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.parentcharacteristictype'),
            preserve_default=False,
        ),
    ]