from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapi.models import Inventory, Coin
from .coins import CoinSerializer



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

        '''
        try:
            coin = Coin.objects.get(pk=1)
            change = coin.coin - 2

            # get single inventory item
            inventory = Inventory.objects.get(pk=pk)
            inventory.quantity = inventory.quantity - 1

            if change >= 0 and inventory.quantity >= 0:

                coin.coin = 0

                coin.save()
                inventory.save()

                response = Response({"quantity": 1}, status=status.HTTP_204_NO_CONTENT)
                response['X-Coins'] = change
                response['X-Inventory-Remaining'] = inventory.quantity

                # return repsonse as JSON
                return response
            elif change < 0: 

                response = Response(status=status.HTTP_403_FORBIDDEN)
                response['X-Coins'] = [coin.coin | 2]
                return response
            
            elif inventory.quantity < 0:
                response = Response(status=status.HTTP_404_NOT_FOUND)
                response['X-Coins'] = coin.coin
                return response


        except Exception as ex:
            # if the item could not be retrived, throw a HTTP server error
            return HttpResponseServerError(ex)