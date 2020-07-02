# Banks-API
REST service that can fetch bank details, using the data given in the API’s query parameters. The RESTful API is written in Django to get any branch details using ifsc code and find all the branches of a bank in a Indian city.

The API is deployed [here](https://banksapi.herokuapp.com/).<br>
1. Given a bank branch IFSC code, get branch details - [banksapi.herokuapp.com/api/banks/?ifsc=IOBA0003450](https://banksapi.herokuapp.com/api/banks/?ifsc=IOBA0003450)
2. Given a bank name and city, gets details of all branches of the bank in the city - [banksapi.herokuapp.com/api/banks/?bank=INDIAN+OVERSEAS+BANK&city=CHENNAI](https://banksapi.herokuapp.com/api/banks/?bank=INDIAN+OVERSEAS+BANK&city=CHENNAI)

## Project Setup
- Create a folder to keep env and clone of the repo.
- Navigate to the folder and setup virtual environment using <br>
```bash
  python -m virtualenv env
 ```
 - Then activate the environment using <br>
  `source env/Scripts/activate` (Use only `env/Scripts/activate` if on cmd or powershell)
- For Linux Users it will be `source env/bin/activate`
- Fork the repo and clone it in the same folder.
- Navigate to the cloned repo and the run the commands:<br>
```bash 
pip install -r requirements.txt
pre-commit install
```
- This will setup the project requirements and pre-commit test hooks!
### Project Directory structure
```bash
   your-folder
   |-env
   |-credicxo
     |-requirements.txt
     |-.pre-commit-config.yaml
     |-
     |-
```
- After the above setup, run <br>
```bash
  python manage.py makemigrations
  python manage.py migrate
```

- Start the backend server
  `python manage.py runserver`
  Runs the backend server at default port `8000`.<br />
  Open [http://localhost:8000](http://localhost:8000) to view it in the browser
  
 - Navigate to [http://localhost:8000/import/](http://localhost:8000/import/) and import the csv file that includes the database of the branches. You can import the database for the Bank Model directly from the admin panel.
   The database can be accessed [here](https://github.com/snarayanank2/indian_banks).
 
