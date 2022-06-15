# Generated by Django 3.2.4 on 2022-01-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='facebook',
            field=models.URLField(default='https://facebook.com/', max_length=500),
        ),
        migrations.AddField(
            model_name='teacher',
            name='gmail',
            field=models.URLField(default='https://gmail.com/', max_length=500),
        ),
        migrations.AddField(
            model_name='teacher',
            name='instagram',
            field=models.URLField(default='https://instagram.com/', max_length=500),
        ),
        migrations.AddField(
            model_name='teacher',
            name='twitter',
            field=models.URLField(default='https://twitter.com/', max_length=500),
        ),
    ]
