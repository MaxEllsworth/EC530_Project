#!/usr/bin/python3

import os
flask_host = "0.0.0.0"
device_templates = "./templates/devices/"
users_template = "./templates/users/"

mongodb_port = 27017
mongodb_address = "localhost"
mongodb_username = "mongodbuser"
mongodb_password = "your_mongodb_root_password"
mongodb_hostname = "localhost"
mongodb_database = "flaskdb"
mongodb_uri = 'mongodb://' + mongodb_username + ':' + mongodb_password + '@' + mongodb_hostname + ':27017/' + mongodb_database


