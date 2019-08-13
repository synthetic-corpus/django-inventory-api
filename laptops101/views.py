from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from laptops101.models import EndUser, Manufacturer
from laptops101 import serializers as s

class EndUserViewSet(viewsets.ViewSet):
    """ CRUD requests for the end user Model. Sending generic replies only. """
    serializer_class = s.EndUserSerializer

    def list(self, request):
        content = {'Message': 'Retrieved List'}
        return Response(content)
    
    def create(self, request):
        return Response({'Message': 'Retrieved List'})
    
    def retrieve(self, request, pk=None):
        """ Retrieves an object. Get crequest. """
        return Response({'http_method': 'GET'})
    
    def update(self, request, pk=None):
        """ Handles updating an object. Put request. """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ A Patch Request. """
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """ Handle removing an object a delete request. """
        return Response({'http_method': 'DELETE'})