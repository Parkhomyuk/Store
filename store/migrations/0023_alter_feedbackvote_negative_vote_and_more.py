# Generated by Django 4.1.1 on 2022-10-27 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_remove_feedback_negative_likes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackvote',
            name='negative_vote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feedbackvote',
            name='positive_vote',
            field=models.BooleanField(default=False),
        ),
    ]