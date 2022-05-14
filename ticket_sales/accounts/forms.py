from .models import User
from django import forms
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    phone_number = forms.CharField(label='شماره تلفن',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    national_code = forms.IntegerField(label='کد ملی', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='رمز عبور',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='نام',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='نام خانوادگی',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('این ایمیل وجود دارد')
        return email
    #
    # def clean(self):
    #     p1 = self.password1
    #     p2 = self.password2
    #
    #     if p1 and p2 and p1 != p2:
    #         raise ValidationError('پسورد وارد شده همخوانی ندارد')
    #     return p1


class LoginForm(forms.Form):
    phone_number = forms.CharField(label='شماره تلفن',
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='رمز عبور',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))