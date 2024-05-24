# Generated by Django 5.0.6 on 2024-05-24 21:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='is_email_verified',
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(db_index=True, error_messages={'unique': 'A user with this email address already exists.'}, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='First name must contain alphabets only.', regex='^[a-zA-Z]+$')]),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(message='Last name must contain alphabets only.', regex='^[a-zA-Z]+$')]),
        ),
    ]