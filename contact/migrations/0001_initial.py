# Generated by Django 4.1.5 on 2023-05-05 13:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ('e_mail', models.EmailField(default='', max_length=254)),
                ('message', models.TextField(max_length=500, validators=[django.core.validators.MinLengthValidator(2)])),
            ],
        ),
    ]