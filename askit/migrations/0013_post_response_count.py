# Generated by Django 2.2.1 on 2020-10-08 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askit', '0012_auto_20200806_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='response_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]