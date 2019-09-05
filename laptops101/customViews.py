from rest_framework.views import viewsets
from rest_framework.response import Response
from rest_framework import status

from laptops101 import serilaizers as s
from laptops101 import models as m

class AssetViewSet(viewsets.ViewSet):
    """ View Set that will retrieve a single items by asset tags """

    def findTable(ASSET_TAG):
        """ 
            Checks each Asset Table and determines if Asset is found
            Returns correct PK and item type if found.
            Returns null if nothing found.

            example: return {pk: 1, type: 'monitor'}
        """
    
    def selectSerializer(self, model, data):
        """ 
            Runs a Serializes Data based on name of Model 
            Returns Serialized Data
        """
        if model == 'laptop':
            """ Serialize as if laptop """
        elif model == 'monitor':
            """ serialize as if monitor """
        else:
            return None
    
    def selectQuery(self, model, pk):
        """
            Returns the queryset from the correct model 
            based on which table the Asset tag was found in.
        """
        if model == 'laptop':
            """ Query laptop model """
        elif model == 'monitor':
            """ Query the monitor Model """
        else:
            return None

    def retrieve(self, request, pk=None):
        """
            Runs the findTable function.
            Returns either a properly serialized table or a 404 error.
        """

        ASSET_TAG = self.request.query_params.get('tag')
        TABLE_INFO = self.findTable(ASSET_TAG)

        if not TABLE_INFO:
            """ Getting a null Response. Return a 404 Error """
            return Response({'error': 'No Assets with tag found', 'data': ASSET_TAG}, status=status.HTTP_400_BAD_REQUEST)
        
        data = self.selectQuery(TABLE_INFO.model, TABLE_INFO.pk)
        serializer = self.selectSerializer(TABLE_INFO.type, data)
        
        if serializer:
            return Response(serializer.data)
        else:
            return Response({'error': 'Internal Code Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)