# Generated by Django 4.0.2 on 2022-04-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_complete_remove_task_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
