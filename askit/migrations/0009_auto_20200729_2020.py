# Generated by Django 2.2.1 on 2020-07-30 03:20

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('askit', '0008_response'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Upvote',
            new_name='Post_Upvote',
        ),
        migrations.RemoveField(
            model_name='response',
            name='upvote_count',
        ),
    ]