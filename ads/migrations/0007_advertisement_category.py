# Generated by Django 4.0.4 on 2022-05-05 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_bidson_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ads.category'),
        ),
    ]
