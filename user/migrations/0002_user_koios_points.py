# Generated by Django 3.2.9 on 2022-06-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='koios_points',
            field=models.IntegerField(default=0, help_text='number of koios points'),
        ),
    ]