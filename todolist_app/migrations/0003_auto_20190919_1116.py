# Generated by Django 2.2.3 on 2019-09-19 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_auto_20190913_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
