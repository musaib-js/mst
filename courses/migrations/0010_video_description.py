# Generated by Django 3.2.4 on 2022-01-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20220121_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.TextField(default='Sorry! The Video Has No Description'),
        ),
    ]