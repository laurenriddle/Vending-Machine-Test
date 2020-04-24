from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapi.models import Inventory



class InventorySerializer(serializers.HyperlinkedModelSerializer):
    '''
    JSON serializer for Inventory
    Arguments: serializers.HyperlinkedModelSerializer
    '''

    class Meta:
        model = Inventory
        url = serializers.HyperlinkedIdentityField(
            view_name='inventory',
            lookup_field='id'
        )
        fields = ('id', 'name', 'quantity')
        depth = 2

class Inventories(ViewSet):
    '''
    
    This class houses functions for List and Retrieve for Inventory
   
    '''

    def retrieve(self, request, pk=None):
        '''
        Handles GET requests for a single industry 
        Returns:
            Response --- JSON serialized industry instance
        To access a single industry: 
        http://localhost:8000/industries/1
        NOTE: Replace the 1 with any ID you wish to retrieve 
        '''
        try:
            # get single industry
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    

    def list(self, request):
        '''
        Handles the GET all requstes to the industry resource
        Returns: 
        Response -- JSON serialized list of industry
        To access all industries: 
        http://localhost:8000/industries
        '''

        # list industries
        inventory = Inventory.objects.all()

        # take response and covert to JSON
        serializer = InventorySerializer(inventory, many=True, context={'request': request})

        # return repsonse as JSON
        return Response(serializer.data)