# Generated by Django 3.0.5 on 2024-03-09 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20240308_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='selected_option',
        ),
    ]