# Generated by Django 5.0.6 on 2024-05-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Название')),
                ('date_create', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Состояние')),
            ],
        ),
    ]
