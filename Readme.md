# User Application

User Application is a simple crud application that stores user data of Parent and Child.
## Features includes-
- Data has first name, last name, address (street, city, state and zip)
- The app creates two User types (Parent, Child). Where The child cannot have an address and must belong to a parent
- App has API to:
  1. Create user data
  2. Show all user data
  3. Update user data
  4. Delete user data

- To store Data, MongoDB is used
- Readme file describing how to install/run the application
- Unit Test

## How to run

(The application is built on the following requirements)
#### Requirements
* Python3.11 (Version is optional)
* pip install pymongo==4.50 - MongoDB Python Driver
* MongoDB 7.0.2 - Database Server
* (Optional)MongoDB Compass 1.40.4 - To view database
* Python dependencies - requirements.txt

#### Steps to follow-
- Create a new folder and copy all the files to the new folder
- Open cmd and go to the folder
- Create a virtual environment and activate it.
```
virtualenv venv //Give any name instead of "venv" 
```
then type "venv/bin/activate" and enter.
```
venv/bin/activate
```
- Install the dependencies
```
pip install -r requirements.txt
```
- Make sure you have mongoDB running in your machine. The Database name is "users_db" and the collection is "users". MongoDB URI- 'mongodb://localhost:27017/users_db'
```
mongodb://localhost:27017/users_db
```

- Then run the main.py file to run the application using the command python main.py (Check if you are in the venv folder before running)
```
python main.py
```
## API Documentation
Considering the application is being run on localhost which can be accessible through http://127.0.0.1:5000.<br>


- To create a new user make a `POST` request to the address "http://127.0.0.1:5000/api/users" with the json document.<br>
### JSON for creating Parent user

```
{
  "user_id": "unique_user_id",
  "user_type": "Parent",
  "first_name": "Asif",
  "last_name": "Chowdhury",
  "address_street": "113 M.M Lane",
  "address_city": "Chandanpura",
  "address_state": "Chattogram",
  "address_zip": "4203"
}
```
### JSON for creating CHILD user
```
{
  "user_id": "unique_user_id",
  "user_type": "Child",
  "first_name": "Aron",
  "last_name": "Jones",
  "parent_id": "existing_parent_id"
}

```

- To show all users make a `GET` request<br>
- To update a user make a `PUT` request with a user_id already in DB <br>
- In order to delete an existing user make a `DELETE` request with an existing user_id