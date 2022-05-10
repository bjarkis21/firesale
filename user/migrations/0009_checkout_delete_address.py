# Generated by Django 4.0.4 on 2022-05-10 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0013_alter_advertisement_reserve'),
        ('user', '0008_remove_userprofile_id_alter_userprofile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=255)),
                ('street_no', models.CharField(max_length=255)),
                ('credid_card_number', models.CharField(max_length=12)),
                ('credid_card_cvc', models.CharField(max_length=4)),
                ('credid_card_expiration_date', models.DateField()),
                ('advertisement', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to='ads.advertisement')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='checkout', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]