# Generated by Django 5.0.7 on 2024-08-12 03:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('profesor', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='profesor',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]