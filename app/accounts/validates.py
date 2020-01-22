from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_password(value):
    box_int = 0
    box_str = 0

    for x in value:
        if x.isdigit():
            box_int += 1
        else:
            box_str += 1

    if len(value) < 8:
        raise ValidationError(
            _('The password should be at least 8 character.'),
            params={'value': value}
        )

    if box_int == 0 or box_str == 0:
        raise ValidationError(
            _('Password need to be at least 1 number and 1 char.'),
            params={'value': value}
        )
