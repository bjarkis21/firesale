# Generated by Django 4.0.4 on 2022-05-04 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0004_alter_advertisement_ispaid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='buyer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
