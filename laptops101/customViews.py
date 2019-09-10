from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from laptops101 import serializers as s
from laptops101 import models as m


class AssetViewSet(APIView):
    """ View Set that will retrieve a single items by asset tags """
    
    def get(self, request, tag=None, format=None):
        return Response({"Hello":"World","tag":tag})
    
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
            Returns either a properly serialized table or a 404 error.
        """

        ASSET_TAG = self.request.query_params.get('tag')
        return Response({'AssetTag': ASSET_TAG}, status.HTTP_200_OK)

        """
        laptop = m.Laptop.objects.filter(ASSET_TAG=ASSET_TAG)
        monitor = m.Monitor.objects.filter(ASSET_TAG=ASSET_TAG)

        if laptop.exists():
            serializer = self.selectSerializer(laptop, laptop)
        elif monitor.exists():
            serializer = self.selectSerializer(laptop, laptop)
        else:
            
            return Response({'error': 'No Assets with tag found', 'data': ASSET_TAG}, status=status.HTTP_404_NOT_FOUND)
        
        if serializer:
            return Response(serializer.data)
        else:
            return Response({'error': 'Internal Code Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        """