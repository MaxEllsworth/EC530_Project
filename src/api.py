#!/usr/bin/python3.8

from flask import Flask, request, jsonify
import logging
#from flask_restx import Api
import variables

from devices import device_blueprint
import users
from users import user_blueprint
from database import MongoClient, mongo_user_wrapper
import uuid

mongodb_port = variables.mongodb_port
mongodb_address = variables.mongodb_address
mongodb_uri = variables.mongodb_uri

flask_host = variables.flask_host
app = Flask(__name__)
app.register_blueprint(device_blueprint)
#api = Api(app)

@app.route("/api/add_user/",methods=["GET", "POST"])
def add_user():
     data = request.json
   #  print('-----')
   #  print(data)
   #  print('-----')
     client = MongoClient(mongodb_uri)
     user_type = data["user_type"]
     attributes = data["attributes"]
     user_uid = data["user_uid"]
     print("user uid is currently " + str(user_uid))
     if (user_type == None):
         user_type = "patient"
     if (attributes == None):
         attributes = {}
     if (user_uid == None):
         user_uid = uuid.uuid4().hex
         logging.info("Assigned user_uid " + str(user_uid))
     logging.info("user_uid is " + str(user_uid))     
     user = users.add_user(user_type, attributes, user_uid)
     print(user.__dict__)
     return jsonify({"uuid" : user_uid})
   
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