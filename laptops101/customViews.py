from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from laptops101 import serializers as s
from laptops101 import models as m


class AssetViewSet(APIView):
    """ View Set that will retrieve a single items by asset tags """
    
    def get(self, request, tag=None, format=None):
        

        laptop = m.Laptop.objects.filter(ASSET_TAG=tag)
        monitor = m.Monitor.objects.filter(ASSET_TAG=tag)

        if laptop.exists():
            data = self.selectSerializer('laptop', laptop)
            return Response(data.data, status=status.HTTP_200_OK)
        elif monitor.exists():
            data = self.selectSerializer('monitor', monitor)
            return Response(data.data, status=status.HTTP_200_OK)
        else:
            return Response({"tag":tag}, status=status.HTTP_404_NOT_FOUND)


    def selectSerializer(self, model, data):
        """ 
            Runs a Serializes Data based on name of Model 
            Returns Serialized Data
        """
        if model == 'laptop':
            """ select laptop serializer. Serialize Data """
            return s.LaptopSerializer(data, many=True)
        elif model == 'monitor':
            """ select monitor serializer. Serialize Data """
            return s.MonitorSerializer(data, many=True)
        else:
            return {"data":"Data is Empty"}