from django import forms
from captcha.fields import CaptchaField
from FormDaftar_app_1174043.models import User

Bank_Choices= [
    ('bca', 'BCA'),
    ('mandiri', 'Mandiri'),
    ('bni', 'BNI'),
    ('bri', 'BRI'),
    ]

class NewUserForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        widgets = {
        'username' : forms.TextInput(attrs={'placeholder': 'Username Account Anda'}),
        'nickname' : forms.TextInput(attrs={'placeholder': 'Tampilan Nama Anda dalam Game'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Password Account Anda'}),
        'retype_Password': forms.PasswordInput(attrs={'placeholder': 'Konfirmasi Password Account Anda'}),
        'email' : forms.TextInput(attrs={'placeholder': 'Email harus Valid dan Benar e.g email_anda@example.com'}),
        'no_Telepon' : forms.TextInput(attrs={'placeholder': 'Nomor Telepon Anda'}),
        'nama_Rekening_Bank' : forms.TextInput(attrs={'placeholder': 'Nama Lengkap Anda Sesuai Buku Tabungan'}),
        'nama_Bank' : forms.Select(choices=Bank_Choices),
        'nomor_Rekening_Bank' : forms.TextInput(attrs={'placeholder': 'Nomor Rekening Bank Anda'}),
        'referral' : forms.TextInput(attrs={'placeholder': 'Nama Referral'}),
        } 
        fields = '__all__'