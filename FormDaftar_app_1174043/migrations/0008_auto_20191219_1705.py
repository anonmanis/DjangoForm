# Generated by Django 2.2.7 on 2019-12-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormDaftar_app_1174043', '0007_user_nomor_rekening_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nomor_Rekening_Bank',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
