from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_test(value):
    """ Test Value. Simply checks if a strings has the letter 'p' in it somewhere """
    if value.find('p') == -1:
        raise ValidationError(
            _('%(value)s does not have the letter p'),
            params={'value': value},
        )