# Generated by Django 2.2.7 on 2019-12-19 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FormDaftar_app_1174043', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='repassword',
            new_name='retype_Password',
        ),
    ]
