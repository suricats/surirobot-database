# Generated by Django 2.1 on 2018-08-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0005_auto_20180712_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='data',
            field=models.TextField(blank=True),
        ),
    ]
