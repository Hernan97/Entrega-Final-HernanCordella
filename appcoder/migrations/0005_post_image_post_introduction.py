# Generated by Django 5.0.7 on 2024-08-15 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]
