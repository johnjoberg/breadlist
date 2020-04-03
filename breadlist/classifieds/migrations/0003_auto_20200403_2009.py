# Generated by Django 3.0.5 on 2020-04-03 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0002_auto_20200403_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classified',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='classified',
            name='time_created',
        ),
        migrations.AddField(
            model_name='classified',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
