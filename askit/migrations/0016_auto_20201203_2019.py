# Generated by Django 2.2.1 on 2020-12-04 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('askit', '0015_auto_20201203_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookie',
            old_name='cookie_count',
            new_name='cookies',
        ),
    ]
