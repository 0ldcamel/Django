# Generated by Django 4.1.13 on 2024-08-30 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create',
            new_name='created',
        ),
    ]
