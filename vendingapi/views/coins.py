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
            view_name='coin',
            lookup_field='id'
        )
        fields = ('id', 'coin')
        depth = 2

class Coins(ViewSet):
    '''
    
    This class houses functions for List and Retrieve for Inventory
   
    '''
    

    def destroy(self, request, pk=None):
        '''
        Handles the GET all requstes to the inventory resource

        Returns: 
        Response -- JSON serialized list of inventory

        To access all inventory: 
        http://localhost:8000/inventory

        '''

        coin = Coin.objects.get(pk=pk)

        current_amount = coin.coin

        coin.coin = 0

        coin.save()

        response = Response(status=status.HTTP_204_NO_CONTENT)
        response['X-Coins'] = current_amount
        # return repsonse as JSON
        return response


    def update(self, request, pk=None):
        '''
        Handles GET requests for a single inventory item

        Returns:
            Response --- JSON serialized inventory instance

        To access a single inventory item: 
        http://localhost:8000/inventory/1

        NOTE: Replace the 1 with any ID you wish to retrieve 
        '''
        
        # get single inventory item
        coin = Coin.objects.get(pk=pk)

        current_amount = coin.coin

        coin.coin = request.data['coin'] + current_amount

        coin.save()

        response = Response(status=status.HTTP_204_NO_CONTENT)
        response['X-Coins'] = coin.coin
        # return repsonse as JSON
        return response
