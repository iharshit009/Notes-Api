# Generated by Django 3.1.4 on 2020-12-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
