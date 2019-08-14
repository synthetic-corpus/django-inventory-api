from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.settings import api_settings

from laptops101.models import EndUser, Manufacturer
from laptops101 import serializers as s

class EndUserViewSet(viewsets.ViewSet):
    """ CRUD requests for the end user Model. Sending generic replies only. """
    serializer_class = s.EndUserSerializer

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}

    def list(self, request):
        queryset = EndUser.objects.all()
        serializer = s.EndUserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = s.EndUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def retrieve(self, request, pk=None):
        queryset = EndUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = s.EndUserSerializer(user)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        """ Handles updating an object. Put request. """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ A Patch Request. """
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """ Handle removing an object a delete request. """
        return Response({'http_method': 'DELETE'})