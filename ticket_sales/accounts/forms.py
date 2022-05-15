from .models import User
from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone_number',
                  'email',
                  'password',
                  'national_code',
                  'first_name',
                  'last_name']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control','id':'id','name':'phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'national_code': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'phone_number': 'شماره تلفن',
            'email': 'ایمیل',
            'password': 'رمز عبور',
            'national_code': 'کد ملی',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }




class LoginForm(forms.Form):
    phone_number = forms.CharField(label='شماره تلفن',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # class Meta:
    #     widgets = {
    #         'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
    #         'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    #     }