# Generated by Django 4.1.1 on 2022-10-19 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_categoryplacetable_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryplacetable',
            name='childId',
        ),
        migrations.AlterField(
            model_name='categoryplacetable',
            name='parentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='store.categorytable'),
        ),
    ]