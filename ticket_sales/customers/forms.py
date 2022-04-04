from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class VerifyPhoneForm(forms.Form):
    verify_code = forms.CharField(max_length=10)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(VerifyPhoneForm, self).__init__(*args, **kwargs)

    def clean_verify_code(self):
        if self.request.session.get('user_register_info', None):
            if self.request.session['user_register_info']['password'] == self.cleaned_data['verify_code']:
                return self.cleaned_data['verify_code']
            else:
                raise ValidationError(_("Invalid verify code!"))
        else:
            raise ValidationError(_("You haven\'t verify code in server! Go to register page and register to get it!"))
