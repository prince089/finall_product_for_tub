# Generated by Django 3.2.9 on 2021-11-18 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduls', '0002_auto_20211118_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equepmentmaster',
            name='plantid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='moduls.plant'),
        ),
    ]
