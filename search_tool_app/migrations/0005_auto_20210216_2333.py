# Generated by Django 3.1.6 on 2021-02-16 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_tool_app', '0004_auto_20210216_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='date_added',
            field=models.DateField(default=datetime.date.today),
        ),
    ]