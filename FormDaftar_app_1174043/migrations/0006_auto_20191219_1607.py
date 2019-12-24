# Generated by Django 2.2.7 on 2019-12-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormDaftar_app_1174043', '0005_auto_20191219_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='*Email Harus Aktif', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='referral',
            field=models.CharField(blank=True, help_text='*Ini tidak wajib di-isi', max_length=128),
        ),
    ]
