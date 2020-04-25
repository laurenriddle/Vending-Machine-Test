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

7. Fire up your dev server and get to work!

	- `python manage.py runserver`

8. Open Postman and test out the API. All requests need to be made to http://localhost:8000. See the documentation below for the requests that can be made to this API. 


## Vend-O-Matic Fetch Calls
_NOTE: All requests are made with a single content type of "application/json"_
### Payment and Reimbursement

- To make a payment to the vending machine, make a PUT request to http://localhost:8000/ with `{ "coin": 1 }` in the body of your request. You will see the number of coins that you currently have inserted into the machine in the response under the X-Coins header. 

- To retrieve all of the coins you have put into the vending machine, make a DELETE request to http://localhost:8000/. You will see the number of coins that you got back in the response under the X-Coins header. 

### Purchasing a Beverage
- 
- 
- 
- 
- 