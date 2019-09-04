""" Django Specific Imports """
from django.db import models

""" customized, app specific imports """
from laptops101 import customValidators as v


class AssetTag(models.Model):
    """ Maintains a list of Asset Tags for sole purpose of input validation across several tables """

    ASSET_TAG = models.CharField(max_length=8, unique=True)

class EndUser(models.Model):

    FIRST_NAME = models.CharField(max_length=100)
    LAST_NAME = models.CharField(max_length=100)
    TITLE = models.CharField(max_length=100)
    EMAIL = models.EmailField(max_length=100, unique=True, blank=True)
    DEPARTMENT = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        """ If e-mail is blank, will auto fill. """
        if bool(self.EMAIL) == False:
            self.EMAIL = self.FIRST_NAME + "." + self.LAST_NAME + '@foobros.net'
        super(EndUser, self).save(*args, **kwargs)


    class Meta:
        unique_together = ["FIRST_NAME", "LAST_NAME"]
        


class Manufacturer(models.Model):
    """ Stores names of Manufacturers and their associated website URLs """
    
    MANUFACTURER = models.CharField(max_length=100, unique=True) # e.g. "Apple" or "Dell"
    WEBSITE = models.CharField(max_length=100)

class ItemArchetype(models.Model):
    """ Static Details about an asset that will not change from item to item 
        e.g. All Dell XPS 4300 will ahve the Same SKU and Manufacturer, but 
        different Serials, Asset Tags, users etc.
    """
    SKU = models.CharField(max_length=100, unique=True)
    COMMON_NAME = models.CharField(max_length=255) # e.g. "Dell XPS"
    MANUFACTURER = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    NOTES = models.CharField(max_length=255)

class TaggedItem(models.Model):
    """ Information common to all Assets, but will change on each asset """
    """ Is the base class for all other items. Will not create its own table """
    
    PURCHASE_DATE = models.DateField(auto_now=False, auto_now_add=True)
    PURCHASE_COST = models.DecimalField(max_digits=7, decimal_places=2)
    ASSIGNED_USER = models.ForeignKey(EndUser, on_delete=models.SET_NULL, null=True)
    ASSET_TAG = models.CharField(max_length=8, unique=True, validators=[v.tag_available])

    def recordAsset(self, tag):
        """ Each time a tagged item is saved, its tag is saved in another table.
            This is done for purpose of input validation. """
        assetTag = AssetTag(ASSET_TAG = self.ASSET_TAG)
        assetTag.save()

    class Meta:
        abstract = True

class Laptop(TaggedItem):
    """ Any Laptop Computer """

    CPU_MODEL = models.CharField(max_length=128) #e.g. Intel i7
    CPU_SPEED = models.DecimalField(max_digits=3, decimal_places=2) # Speed of CPU in GHZ
    RAM = models.IntegerField() # RAM in GB
    HDD = models.DecimalField(max_digits=4, decimal_places = 2) # HDD size in Terabytes
    ARCHETYPE = models.ForeignKey(ItemArchetype, on_delete=models.CASCADE,)
    NOTES = models.CharField(max_length=255, default="Notes can be added here.")

    def save(self, *args, **kwargs):
        """ Ivokes a method to copy the asset tag to the asset tag table """
        self.recordAsset(self.ASSET_TAG)
        super(Laptop, self).save(*args, **kwargs)

class Monitor(TaggedItem):
    """ Any monitored deployed with a laptop """

    HDMI = models.BooleanField(default=True)
    VGA = models.BooleanField(default=False)
    DISPLAY_PORT = models.BooleanField(default=True)
    ARCHETYPE = models.ForeignKey(ItemArchetype, on_delete=models.CASCADE,)
    NOTES = models.CharField(max_length=255, default="Notes can be added here.")

    def save(self, *args, **kwargs):
        """ Ivokes a method to copy the asset tag to the asset tag table """
        self.recordAsset(self.ASSET_TAG)
        super(Monitor, self).save(*args, **kwargs)