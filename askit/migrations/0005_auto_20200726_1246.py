# Generated by Django 2.2.1 on 2020-07-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('askit', '0004_remove_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(),
        ),
    ]