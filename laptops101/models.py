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

class GenericItem(models.Model):
    """ All Items in inventory will have an asset tag, SKU, and Serial number.
        SKU Uniquely identifies the type of item from manufacturer.
        Serial is the manufactuer's serial.
        Asset tag is internal to the company using this database. """
    
    SKU = models.CharField(max_length=255)
    SERIAL = models.CharField(max_length=255)
    ASSET = models.CharField(max_length=30)
    MANUFACTURER = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    PURCHASE_DATE = models.DateField(_(""), auto_now=False, auto_now_add=False)
    PURCHASE_COST = models.DecimalField(max_digits=7, decimal_places=2)
    ASSIGNED_USER = models.ForeignKey(EndUser, on_delete=models.SET_NULL)

class Laptop(models.Model):
    """ Any Laptop Computer """
    CPU_MODEL = models.CharField(max_length=128) #e.g. Intel i7
    CPU_SPEED = models.DecimalField(max_digits=3, decimal_places=2) # Speed of CPU in GHZ
    RAM = models.IntegerField() # RAM in GB
    HDD = models.DecimalField(max_digits=4, decimal_places = 2) # HDD size in Terabytes
    COMMON_ATTRIBUTES = models.ForeignKey(GenericItem, on_delete=models.CASCADE)