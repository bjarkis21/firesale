# Generated by Django 4.0.4 on 2022-05-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0017_advertisement_condition1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='condition',
        ),
    ]
