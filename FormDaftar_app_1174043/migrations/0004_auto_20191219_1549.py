# Generated by Django 2.2.7 on 2019-12-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormDaftar_app_1174043', '0003_auto_20191219_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nama_Bank',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='nama_Rekening_Bank',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='no_Telepon',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='retype_Password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128),
        ),
    ]
