from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapi.models import Coin

class CoinSerializer(serializers.HyperlinkedModelSerializer):
    '''
    JSON serializer for Coins
    Arguments: 
        serializers.HyperlinkedModelSerializer
    '''

    class Meta:
        model = Coin
        url = serializers.HyperlinkedIdentityField(
            view_name='coin',
            lookup_field='id'
        )
        fields = ('id', 'coin')

class Coins(ViewSet):
    '''
    Handles the views for the Coins endpoint
    Arguments: 
        ViewSet
    '''
    
    def destroy(self, request, pk=None):
        '''
        Handles the DELETE requests for a single coin
        Returns: 
            Response -- Header with number of coins to be returned and HTTP 204 status code 
        '''
        try:
            coin = Coin.objects.get(pk=pk)

            coin.delete() 

            return Response(headers={'X-Coins': coin.coin}, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return HttpResponseServerError(ex)


    def update(self, request, pk=None):
        '''
        Handles the PUT requests for a single coin
        Returns:
            Response --- Header with number of coins that are currently in the machine and HTTP 204 status code
        '''
        try:
            coin = Coin.objects.get(pk=pk)
            if request.data['coin'] == 1: # make sure the user is only inserting one coin at a time
                coin.coin += 1 # insert a single coin into the machine every time the update method is called
                coin.save()
                return Response(headers={'X-Coins': coin.coin}, status=status.HTTP_204_NO_CONTENT)
            else: # if the user tried to insert more than 1 coin, we do not add additional coins to the DB
                return Response(headers={'X-Coins': coin.coin}, status=status.HTTP_204_NO_CONTENT)

        except Exception as ex:
            return HttpResponseServerError(ex)
