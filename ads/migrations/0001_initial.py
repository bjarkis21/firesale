# Generated by Django 4.0.4 on 2022-05-02 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('long_description', models.CharField(max_length=9999)),
                ('condition', models.CharField(max_length=255)),
                ('image', models.CharField(blank=True, max_length=500)),
                ('reserve', models.IntegerField(blank=True)),
                ('creation_date', models.DateTimeField()),
                ('rating', models.FloatField(blank=True)),
                ('buy_date', models.DateTimeField(blank=True)),
                ('isPaid', models.BooleanField()),
                ('isSold', models.BooleanField()),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer', to='user.userprofile')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BidsOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('bid_date', models.DateTimeField()),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.advertisement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
        migrations.AddConstraint(
            model_name='bidson',
            constraint=models.UniqueConstraint(fields=('user', 'advertisement', 'amount'), name='keyConstraint'),
        ),
    ]
