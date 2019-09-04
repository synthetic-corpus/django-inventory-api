from django.core.exceptions import ValidationError
from django.db import models
from laptops101 import models
from django.utils.translation import gettext_lazy as _

def tag_available(value):
    """ Checks if value already in Asset Tags and therefore used. """
    querySet = models.AssetTag.objects.values_list('ASSET_TAG')
    if querySet.filter(ASSET_TAG=value).exists():
        """ e.g. if a record is found with the value already... """
        raise ValidationError(
            _('%(value)s is already recorded as in use'),
            params={'value': value},
        )