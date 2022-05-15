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
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
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

        help_texts = {
            'phone_number': 'این شماره تلفن از قبل ثبت شده است، لطفا شماره تلفن معتبر را وارد کنید',
            'email': 'ایمیل منحصر به فرد وارد کنید',
            'national_code': 'کاربر با این کد ملی وجود دارد',

        }

        # def clean_email(self):
        #     email = self.cleaned_data['email']
        #     user = User.objects.filter(email=email).exists()
        #     if user:
        #         raise ValidationError('این ایمیل وجود دارد')
        #     return email
        #
        # def clean_phone_number(self):
        #     phone_number = self.cleaned_data['phone_number']
        #     user = User.objects.filter(phone_number=phone_number).exists()
        #     if user:
        #         return ValidationError('این شماره تلفن قبلا ثبت شده است')
        #     return phone_number



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