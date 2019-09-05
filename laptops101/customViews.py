from rest_framework.views import viewsets
from rest_framework.response import Response
from rest_framework import status

from laptops101 import serilaizers as s
from laptops101 import models as m

class AssetViewSet(viewsets.ViewSet):
    """ View Set that will retrieve a single items by asset tags """
    
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

    def retrieve(self, request, pk=None):
        """
            Runs the findTable function.
            Returns either a properly serialized table or a 404 error.
        """

        ASSET_TAG = self.request.query_params.get('tag')
        TABLE_INFO = self.findTable(ASSET_TAG)

        laptop = m.laptop.objects.filter(ASSET_TAG=ASSET_TAG)
        monitor = m.monitor.objects.filter(ASSET_TAG=ASSET_TAG)

        if laptop.exists():
            serializer = self.selectSerializer(laptop, laptop)
        elif monitor.exists():
            serializer = self.selectSerializer(laptop, laptop)
        else:
            """ Return a 404 Error """
            return Response({'error': 'No Assets with tag found', 'data': ASSET_TAG}, status=status.HTTP_404_NOT_FOUND)
        
        if serializer:
            return Response(serializer.data)
        else:
            return Response({'error': 'Internal Code Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)