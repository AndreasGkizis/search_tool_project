# Generated by Django 3.1.6 on 2022-05-26 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_tool_app', '0002_language_language_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='language_code',
        ),
    ]
