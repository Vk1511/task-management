# Generated by Django 5.0.6 on 2024-05-25 07:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usertask',
            unique_together={('title', 'created_by')},
        ),
        migrations.CreateModel(
            name='TaskComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_at', models.DateTimeField(auto_now=True)),
                ('comment_updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_tickets.usertask')),
            ],
        ),
        migrations.CreateModel(
            name='SharedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('shared_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_by_user', to=settings.AUTH_USER_MODEL)),
                ('shared_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_with_user', to=settings.AUTH_USER_MODEL)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task_tickets.usertask')),
            ],
            options={
                'unique_together': {('task_id', 'shared_with', 'shared_by')},
            },
        ),
    ]
