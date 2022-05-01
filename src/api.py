#!/usr/bin/python3.8

from flask import Flask
#from flask_restx import Api
import variables

from devices import device_blueprint
from users import user_blueprint
from database import mongo_user_wrapper

mongodb_port = variables.mongodb_port
mongodb_address = variables.mongodb_address
mongodb_uri = variables.mongodb_uri

flask_host = variables.flask_host
app = Flask(__name__)
app.register_blueprint(device_blueprint)
#api = Api(app)

@app.route("/api/add_user/")
def add_user():
    client = MongoClient(mongodb_uri)
    user = users.add_user(collection_name, attributes, user_uid = "",)

    True
'''
@app.route("/api/delete_user")
def delete_user():
    True

@app.route("/api/update_user")
def update_user():
    True

@app.route("/api/assign_device_to_user")
def assign_device_to_user():
    True

@app.route("/api/remove_device_from_user")
def remove_device_from_user():
    True

@app.route("/api/list_available_devices")
def list_available_devices():
    True
'''

if __name__ == "__main__":
    app.run(host=flask_host)#, ssl_context='adhoc')