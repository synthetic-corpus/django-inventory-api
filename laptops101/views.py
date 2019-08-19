from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.settings import api_settings

from laptops101.models import EndUser, Manufacturer
from laptops101 import serializers as s

class EndUserViewSet(viewsets.ModelViewSet):
    """ Handles the updating and paths for end users """
    serializer_class = s.EndUserSerializer
    queryset = EndUser.objects.all()

class ManufacturerViewSet(viewsets.ModelViewSet):
    """ Handles CRUD for manufactuers """
    serializer_class = s.ManufacturerSerializer
    queryset = Manufacturer.objects.all()