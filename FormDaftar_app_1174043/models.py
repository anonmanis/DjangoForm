from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    nickname = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=50)
    retype_Password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, help_text="*Email Harus Aktif", unique=True)
    no_Telepon = models.CharField(max_length=20, unique=True)
    nama_Rekening_Bank = models.CharField(max_length=128)
    nama_Bank = models.CharField(max_length=50)
    nomor_Rekening_Bank = models.CharField(max_length=50, unique=True)
    referral = models.CharField(max_length=128, blank=True, help_text="*Ini tidak wajib di-isi")