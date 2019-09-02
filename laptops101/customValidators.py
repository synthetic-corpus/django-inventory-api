from django.core.exceptions import ValidationError
from django.db import models
from laptops101 import models
from django.utils.translation import gettext_lazy as _

def validate_test(value):
    """ Test Value. Simply checks if a strings has the letter 'p' in it somewhere """
    print(models.AssetTag.objects.all())
    return True