# Generated by Django 3.1 on 2020-08-25 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200825_1902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boxs',
            options={'get_latest_by': 'NumberBox'},
        ),
    ]
