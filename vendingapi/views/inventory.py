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
        Handles GET requests for a single inventory item

        Returns:
            Response --- JSON serialized inventory instance

        To access a single inventory item: 
        http://localhost:8000/type object 'Inventory' has no attribute 'objects'/1

        NOTE: Replace the 1 with any ID you wish to retrieve 
        '''
        try:
            # get single inventory item
            inventory = Inventory.objects.get(pk=pk)

            # take response and covert to JSON
            serializer = InventorySerializer(inventory, context={'request': request})

            # return repsonse as JSON
            return Response(serializer.data)

        except Exception as ex:
            # if the item could not be retrived, throw a HTTP server error
            return HttpResponseServerError(ex)
    

    def list(self, request):
        '''
        Handles the GET all requstes to the inventory resource

        Returns: 
        Response -- JSON serialized list of inventory

        To access all inventory: 
        http://localhost:8000/inventory

        '''

        # list inventory
        inventory = Inventory.objects.all() 

        # take response and covert to JSON
        serializer = InventorySerializer(inventory, many=True, context={'request': request})

        # return repsonse as JSON
        return Response(serializer.data)


    def update(self, request, pk=None):
        '''
        Handles GET requests for a single inventory item

        Returns:
            Response --- JSON serialized inventory instance

        To access a single inventory item: 
        http://localhost:8000/type object 'Inventory' has no attribute 'objects'/1

        NOTE: Replace the 1 with any ID you wish to retrieve 
        '''
        try:
            # get single inventory item
            inventory = Inventory.objects.get(pk=pk)

            # take response and covert to JSON
            serializer = InventorySerializer(inventory, context={'request': request})

            # return repsonse as JSON
            return Response(serializer.data)

        except Exception as ex:
            # if the item could not be retrived, throw a HTTP server error
            return HttpResponseServerError(ex)