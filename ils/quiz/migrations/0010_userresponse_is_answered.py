# Generated by Django 3.0.5 on 2024-05-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_auto_20240523_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
    ]
