# Generated by Django 3.2 on 2021-04-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1234-12-31'),
            preserve_default=False,
        ),
    ]
