# Generated by Django 3.1.6 on 2022-06-07 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_tool_app', '0003_remove_language_language_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='papers/pdfs'),
        ),
    ]
