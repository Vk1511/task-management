# Generated by Django 5.0.6 on 2024-05-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tickets', '0003_usertask_assigned_at_usertask_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskcomments',
            name='comment_at',
            field=models.DateTimeField(),
        ),
    ]
