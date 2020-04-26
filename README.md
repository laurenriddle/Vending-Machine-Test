# Vend-O-Matic
## Want to use Vend-O-Matic? Follow the steps below to set it up.

1. Clone down this repository by running the following command in your terminal `git clone git@github.com:laurenriddle/Vending-Machine-Test.git`.
2. After the clone is finished, run `cd Vending-Machine-Test` in your terminal. 
3. Create your virtual environment by typing the following commands in your terminal:
    - For OSX: 
        - `python -m venv VendingEnv`
        - `source ./VendingEnv/bin/activate`

    - For Windows:
        - `python -m venv VendingEnv`
        - `source ./VendingEnv/Scripts/activate`

4. Install the app's dependencies:

	- `pip install -r requirements.txt`

5. Build your database from the existing models:

	- `python manage.py makemigrations vendingapi`
	- `python manage.py migrate`


6. Populate your database with initial data from fixtures files: (_NOTE: every time you run this it will remove existing data and repopulate the tables_)

	- `python manage.py loaddata */fixtures/*.json`

7. Fire up your server and get to work!

	- `python manage.py runserver`

8. Use Postman to test the application. See the documentation below for the requests that can be made to this API. 


## Vend-O-Matic Fetch Calls
_NOTE: All requests are made to http://localhost:8000 with a single content type of "application/json"_
### Payment and Reimbursement

- To make a payment to the vending machine, make a PUT request to http://localhost:8000/1 with `{ "coin": 1 }` in the body of your request. You will see the number of coins that are currently inserted into the machine in the response under the X-Coins header. _NOTE: If you send more than 1 coin to the machine (e.g. `{ "coin": 5 }`), then 0 coins will be inserted into the machine. You can only insert 1 coin at a time._

- To retrieve all of the coins you have put into the vending machine, make a DELETE request to http://localhost:8000/1. You will see the number of coins that you got back in the response under the X-Coins header. _NOTE: Once you have deleted your coins, you will have to go into TablePlus (or your DB editor of choice) and manually add another coin instance. If the new coin that you add has a different id than 1, replace the 1 in the request URL with the ID of your current coin instance._

### Purchasing a Beverage
- To retrieve a list of the beverage quantities left in the machine, make a GET request to http://localhost:8000/inventory. You will recieve an array of remaining inventory in the body of the response that looks like this: `{ "remaining inventory": [ 4, 5, 3 ] }`.
- To retrieve the remaining quantity of a single beverage, make a GET request to http://localhost:8000/inventory/:id (where :id is the id of whichever beverage you wish to retrieve). You will recieve a single integer representing the current beverage quantity in the body of the response.
- To purchase a beverage, make a PUT request to http://localhost:8000/inventory/:id (where :id is the id of whichever beverage you wish to purchase). If you have given the machine enough money AND there are beverages in stock, you will see the number of coins that you recieved as change from your transaction in the response under the X-Coins header. You will also see the amount of beverages remaining in inventory under the X-Inventory-Remaining header and you will see the quantity of drinks that you bought in the body of the repsponse. 
    - _Exception 1: If you have not inserted enough coins into the machine, you will receive a 403 response code and in the X-Coins header you will see how many coins you have inserted and how many you need total to purchase a drink (e.g. 1/2)._
    - _Exception 2: If the beverage you wish to purchase is out of stock, you will recieve a 404 response code and in the X-Coins header you will see how many coins you have inserted into the machine._