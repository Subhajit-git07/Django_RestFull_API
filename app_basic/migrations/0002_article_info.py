# Generated by Django 2.1.3 on 2020-09-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='info',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
