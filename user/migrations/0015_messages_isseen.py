# Generated by Django 4.0.4 on 2022-05-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_checkout_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='isSeen',
            field=models.BooleanField(default=False),
        ),
    ]
