# Generated by Django 3.2.9 on 2021-11-19 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moduls', '0007_auto_20211119_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='sitecity',
            field=models.CharField( max_length=50),
            preserve_default=False,
        ),
    ]
