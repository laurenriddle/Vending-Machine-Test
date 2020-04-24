from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapi.models import Coin



class CoinSerializer(serializers.HyperlinkedModelSerializer):
    '''
    JSON serializer for Inventory
    Arguments: serializers.HyperlinkedModelSerializer
    '''

    class Meta:
        model = Coin
        url = serializers.HyperlinkedIdentityField(
            view_name='',
            lookup_field='id'
        )
        fields = ('id', 'coins')
        depth = 2

class Coins(ViewSet):
    '''
    
    This class houses functions for List and Retrieve for Inventory
   
    '''
    

    # def destroy(self, request):
    #     '''
    #     Handles the GET all requstes to the inventory resource

    #     Returns: 
    #     Response -- JSON serialized list of inventory

    #     To access all inventory: 
    #     http://localhost:8000/inventory

    #     '''

    #     # list inventory
    #     inventory = Inventory.objects.all() 

    #     # take response and covert to JSON
    #     serializer = InventorySerializer(inventory, many=True, context={'request': request})

    #     # return repsonse as JSON
    #     return Response(serializer.data)


    def update(self, request, pk=None):
        '''
        Handles GET requests for a single inventory item

        Returns:
            Response --- JSON serialized inventory instance

        To access a single inventory item: 
        http://localhost:8000/ 

        NOTE: Replace the 1 with any ID you wish to retrieve 
        '''
        try:
            coin = Coin.objects.get(pk=1)
            print(request, "HELLO")
            # return repsonse as JSON
            response = Response()
            response["testing"] = "gey"
            return response

        except Exception as ex:
            # if the item could not be retrived, throw a HTTP server error
            return HttpResponseServerError(ex)