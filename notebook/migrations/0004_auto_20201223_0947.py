# Generated by Django 3.1.4 on 2020-12-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_auto_20201223_0642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name_plural': 'Notes'},
        ),
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
