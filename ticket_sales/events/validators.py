import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_iran_national_code(national_code):
    if not re.search(r'^\d{10}$', national_code):
        raise ValidationError(_('کدملی وارد شده معتبر نمیباشد.'))
    check = int(national_code[9])
    s = sum(int(national_code[x]) * (10 - x) for x in range(9)) % 11
    if s < 2:
        if check != s:
            raise ValidationError(_('کدملی وارد شده معتبر نمیباشد.'))
    elif check + s != 11:
        raise ValidationError(_('کدملی وارد شده معتبر نمیباشد.'))
