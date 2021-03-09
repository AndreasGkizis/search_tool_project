# Generated by Django 3.1.6 on 2021-03-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_tool_app', '0008_auto_20210223_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='pdf',
            field=models.FileField(null=True, upload_to='papers/pdfs'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(max_length=1000, null=True, unique=True),
        ),
    ]
