# Generated by Django 3.1.6 on 2022-07-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_tool_app', '0004_auto_20220607_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
