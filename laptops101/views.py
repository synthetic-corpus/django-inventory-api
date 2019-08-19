from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.settings import api_settings

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
