# Generated by Django 4.0.4 on 2022-05-11 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_messages_isseen'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='isNewMessage',
            field=models.BooleanField(default=False),
        ),
    ]
