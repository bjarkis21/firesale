# Generated by Django 4.0.4 on 2022-05-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0017_alter_advertisement_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='condition',
            field=models.CharField(default='', max_length=255),
        ),
    ]
