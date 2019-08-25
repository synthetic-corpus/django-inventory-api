from rest_framework import serializers as s
from laptops101 import models as m

class EndUserSerializer(s.ModelSerializer):
    """ Serializer an EndUser Model from models """

    class Meta:
        model = m.EndUser
        fields = ('FIRST_NAME', 'LAST_NAME', 'TITLE', 'DEPARTMENT', 'EMAIL')

class ManufacturerSerializer(s.ModelSerializer):
    """ Serializer for manufacturers """

    class Meta:
        model = m.Manufacturer
        fields = ('MANUFACTURER', 'WEBSITE')

class ItemArchetypeSerializer(s.ModelSerializer):
    """ Serializes an Archetype """

    class Meta:
        model = m.ItemArchetype
        fields = ('SKU', 'COMMON_NAME', 'MANUFACTURER', 'NOTES')

class LaptopSerializer(s.ModelSerializer):
    """ Serializes a laptop """

    class Meta:
        model = m.Laptop
        fields = ('CPU_MODEL', 'CPU_SPEED', 'RAM', 
                    'HDD', 'ARCHETYPE', 'NOTES',
                    'PURCHASE_DATE','PURCHASE_COST',
                    'ASSIGNED_USER','ASSET_TAG')

class MonitorSerializer(s.ModelSerializer):
    """ Serializes a Monitor """

    class Meta:
        model = m.Monitor
        fields = ('HDMI', 'VGA', 'DISPLAY_PORT', 
                    'ARCHETYPE', 'NOTES',
                    'PURCHASE_DATE','PURCHASE_COST',
                    'ASSIGNED_USER','ASSET_TAG')