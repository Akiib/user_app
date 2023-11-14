from flask import Flask
from flask_pymongo import PyMongo
from controller import create_user, get_all_users, update_user, delete_user

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/users_db'
mongo = PyMongo(app)

# Connect the controller functions to the app and mongo

create_user(app, mongo)
get_all_users(app,mongo)
update_user(app, mongo)
delete_user(app, mongo)

if __name__ == '__main__':
    app.run(debug=True)
