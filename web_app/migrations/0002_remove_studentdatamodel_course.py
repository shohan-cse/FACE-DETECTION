# Generated by Django 4.0.4 on 2022-05-21 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdatamodel',
            name='course',
        ),
    ]
