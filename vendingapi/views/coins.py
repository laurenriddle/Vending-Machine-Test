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

class Coins(ViewSet):
    
    def destroy(self, request, pk=None):
        '''
        Handles the DELETE requests for a single coin
        Returns: 
        Response -- Header with number of coins to be returned and HTTP 204 status code 
        '''
        try:
            coin = Coin.objects.get(pk=pk)

            change = coin.coin # calculates change to be returned

            coin.coin = 0 # sets the value of the coins in the vending machine to 0

            coin.save() # instead of actually "deleting" the coin instance, I chose to set the value of the coin to 0 again so the user can keep adding coins to the DB and purchasing more items. 
            # NOTE: If we wish to actually delete the coin from the DB, we could just replace lines 35 - 37 with "coin.delete()". The disadvantage to deleting the coin is that the user will have to go into the DB and create a new coin instance to purchase more items.

            return Response(headers={'X-Coins': change}, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return HttpResponseServerError(ex)


    def update(self, request, pk=None):
        '''
        Handles PUT requests for a single coin
        Returns:
            Response --- Header with number of coins that are currently in the machine and HTTP 204 status code
        '''
        try:
            coin = Coin.objects.get(pk=pk)
            coin.coin += 1 # insert a single coin into the machine every time the update method is called
            coin.save()
            return Response(headers={'X-Coins': coin.coin}, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return HttpResponseServerError(ex)
