# Generated by Django 4.0.4 on 2022-05-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_userprofile_isnewmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.CharField(default='https://static.vecteezy.com/system/resources/previews/002/318/271/original/user-profile-icon-free-vector.jpg', max_length=9999),
        ),
    ]
