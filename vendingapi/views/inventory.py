from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from vendingapi.models import Inventory, Coin

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    '''
    JSON serializer for Inventory
    Arguments: 
        serializers.HyperlinkedModelSerializer
    '''

    class Meta:
        model = Inventory
        url = serializers.HyperlinkedIdentityField(
            view_name='inventory',
            lookup_field='id'
        )
        fields = ('id', 'name', 'quantity')


class Inventories(ViewSet):
    '''
    Handles the views for the Inventories endpoint
    Arguments: 
        ViewSet
    '''

    def retrieve(self, request, pk=None):
        '''
        Handles GET requests for a single inventory item
        Returns:
            Response --- integer representing remaining quantity of a single beverage and an HTTP 200 status code

        '''
        try:
            inventory = Inventory.objects.get(pk=pk)
        
            return Response(inventory.quantity, status=status.HTTP_200_OK)

        except Exception as ex:
            return HttpResponseServerError(ex)
    

    def list(self, request):
        '''
        Handles the GET requests to the inventory resource
        Returns: 
            Response -- list of current beverage inventory numbers and an HTTP 200 status code

        '''

        inventory = Inventory.objects.all() 

        current_inventory = [ beverage.quantity for beverage in inventory ] # creates a list of beverage quantities available
        
        return Response({"remaining inventory": current_inventory}, status=status.HTTP_200_OK)


    def update(self, request, pk=None):
        '''
        Handles PUT requests for a single beverage
        Returns:
            Response --- Custom X-Coins header, quantity of beverages purchased, and either an HTTP 204, 404, or 403 status code

        '''
        try:

            coins = Coin.objects.all()
            inventory = Inventory.objects.get(pk=pk)

            if len(coins) <= 0: # checks to make sure there is a coin instance in the DB
                return Response(headers={'X-Coins': f"0 / 2"}, status=status.HTTP_403_FORBIDDEN)
            
            else: # if there is a coin instance in the DB
                for coin in coins: 
                    change = coin.coin - 2 # calculates possible change for transaction

                    if change < 0: # if the customer has not inserted enough money to buy a beverage
                        return Response(headers={'X-Coins': f"{coin.coin} / 2"}, status=status.HTTP_403_FORBIDDEN)
                    
                    elif inventory.quantity - 1 < 0: # if there are no more beverages in stock
                        return Response(headers={'X-Coins': coin.coin}, status=status.HTTP_404_NOT_FOUND)

                    elif change >= 0 and inventory.quantity >= 0: # if the customer has inserted enough money to buy a beverage

                        inventory.quantity -= 1 # subtracts items bought from current quantity
                        coin.coin = 0 # resets amount of coins in machine to 0

                        coin.save()
                        inventory.save()

                        return Response({"quantity": 1}, headers={'X-Coins': change, 'X-Inventory-Remaining': inventory.quantity}, status=status.HTTP_200_OK)
                    
        except Exception as ex:
            return HttpResponseServerError(ex)