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
     client = MongoClient(mongodb_uri)
     user_type = request.form.get("user_type")
     attributes = request.form.get("attributes")
     user_uid = request.form.get("user_uid")
     if (user_type == None):
         user_type = "patient"
     if (attributes == None):
         attributes = {}
     if (user_uid == None):
         user_uid = uuid.uuid4().hex
         logging.info("Assigned user_uid " + str(user_uid))
     logging.info("user_uid is " + str(user_uid))     
     user = users.add_user(user_type, attributes, user_uid)
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