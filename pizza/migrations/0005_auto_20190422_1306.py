# Generated by Django 2.2 on 2019-04-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20190422_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='count',
        ),
        migrations.AddField(
            model_name='component',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]