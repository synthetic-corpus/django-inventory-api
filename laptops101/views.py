from rest_framework import viewsets


from laptops101 import models as m
from laptops101 import serializers as s

class EndUserViewSet(viewsets.ModelViewSet):
    """ Handles the updating and paths for end users """
    serializer_class = s.EndUserSerializer
    queryset = m.EndUser.objects.all()

class ManufacturerViewSet(viewsets.ModelViewSet):
    """ Handles CRUD for manufactuers """
    serializer_class = s.ManufacturerSerializer
    queryset = m.Manufacturer.objects.all()

class ItemArchetypeViewSet(viewsets.ModelViewSet):
    """ View set for itemArchetypes """
    serializer_class = s.ItemArchetypeSerializer
    queryset = m.ItemArchetype.objects.all()

class LaptopViewSet(viewsets.ModelViewSet):
    """ View of all Laptops """
    serializer_class = s.LaptopSerializer
    queryset = m.Laptop.objects.all()

class MonitorViewSet(viewsets.ModelViewSet):
    """ View of all Monitors """
    serializer_class = s.MonitorSerializer
    queryset = m.Monitor.objects.all()

