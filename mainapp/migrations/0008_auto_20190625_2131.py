# Generated by Django 2.2.1 on 2019-06-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20190625_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='content',
            field=models.CharField(max_length=200),
        ),
    ]
