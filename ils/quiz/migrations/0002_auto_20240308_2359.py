# Generated by Django 3.0.5 on 2024-03-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userresponse',
            name='user',
        ),
        migrations.AddField(
            model_name='userresponse',
            name='difficulty_rating',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
