# Generated by Django 4.0.4 on 2022-05-09 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_alter_bidson_advertisement_alter_bidson_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
