# Generated by Django 2.2.4 on 2019-09-30 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_manager',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_user',
        ),
    ]