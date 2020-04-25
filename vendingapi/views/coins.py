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
    
    def destroy(self, request, pk=None):
        '''
        Handles the DELETE requests to the coins endpoint
        Returns: 
        Response -- JSON serialized list of inventory
        '''
        coin = Coin.objects.get(pk=1)
        change = coin.coin
        coin.coin = 0
        coin.save()
        return Response(headers={'X-Coins': change}, status=status.HTTP_204_NO_CONTENT)


    def update(self, request, pk=None):
        '''
        Handles PUT requests for a single coin
        Returns:
            Response --- JSON serialized inventory instance
        '''
        # get single coin item
        coin = Coin.objects.get(pk=1)
        coin.coin += 1
        coin.save()
        return Response(headers={'X-Coins': coin.coin}, status=status.HTTP_204_NO_CONTENT)
