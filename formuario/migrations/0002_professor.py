# Generated by Django 4.2.2 on 2023-06-21 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('disciplina', models.CharField(max_length=250)),
            ],
        ),
    ]