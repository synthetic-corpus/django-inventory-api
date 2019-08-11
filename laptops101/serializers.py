from rest_framework import serializers as s
from laptops101 import models

class EndUserSerializer(s.ModelSerializer):
    """ Serializer an EndUser Model from models """

    class Meta:
        model = models.EndUser
        fields = ('FIRST_NAME', 'LAST_NAME', 'TITLE', 'DEPARTMENT')

class ManufacturerSerializer(s.ModelSerializer):
    """ Serializer for manufacturers """

    class Meta:
        model = models.Manufacturer
        fields = ('MANUFACTURER', 'WEBSITE')