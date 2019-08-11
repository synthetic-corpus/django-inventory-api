""" Django Specific Imports """
from django.db import models

class EndUser(models.Model):
    FIRST_NAME = models.CharField(max_length=255)
    LAST_NAME = models.CharField(max_length=255)
    TITLE = models.CharField(max_length=255)
    DEPARTMENT = models.CharField(max_length=255)

class Manufacturer(models.Model):
    """ Stores names of Manufacturers and their associated website URLs """
    
    MANUFACTURER = models.CharField(max_length=255) # e.g. "Apple" or "Dell"
    WEBSITE = models.CharField(max_length=255)

class ItemArchetype(models.Model):
    """ Static Details about an asset that will not change from item to item 
        e.g. All Dell XPS 4300 will ahve the Same SKU and Manufacturer, but 
        different Serials, Asset Tags, users etc.
    """
    SKU = models.CharField(max_length=255)
    COMMON_NAME = models.CharField(max_length=255) # e.g. "Dell XPS"
    MANUFACTURER = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    NOTES = models.CharField(max_length=255)

class TagInformation(models.Model):
    """ Information common to all Assets, but will change on each asset """

    PURCHASE_DATE = models.DateField(auto_now=False, auto_now_add=False)
    PURCHASE_COST = models.DecimalField(max_digits=7, decimal_places=2)
    ASSIGNED_USER = models.ForeignKey(EndUser, on_delete=models.SET_NULL, null=True)
    ASSET_TAG = models.CharField(max_length=8)

class Laptop(models.Model):
    """ Any Laptop Computer """

    CPU_MODEL = models.CharField(max_length=128) #e.g. Intel i7
    CPU_SPEED = models.DecimalField(max_digits=3, decimal_places=2) # Speed of CPU in GHZ
    RAM = models.IntegerField() # RAM in GB
    HDD = models.DecimalField(max_digits=4, decimal_places = 2) # HDD size in Terabytes
    ARCHETYPE = models.ForeignKey(ItemArchetype, on_delete=models.CASCADE,)
    TAG = models.ForeignKey(TagInformation, on_delete=models.CASCADE,)
    NOTES = models.CharField(max_length=255)