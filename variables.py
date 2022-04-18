#!/usr/bin/python3

import os
flask_host = "0.0.0.0"
device_templates = "./templates/devices/"
users_template = "./templates/users/"

mongodb_port = 27017
mongodb_address = "172.17.0.1"#"localhost"
mongodb_username = "mongoadmin"
mongodb_password = "secret"
mongodb_hostname = "localhost"
mongodb_database = "flaskdb"
mongodb_uri = 'mongodb://' + mongodb_username + ':' + mongodb_password + '@' + mongodb_address + ':' + str(mongodb_port) + '/' + mongodb_database + "?authSource=admin"


audio_dir = "./audio/"
original_audio_dir = audio_dir + "./originals/"
chunk_audio_dir = audio_dir + "./chunks/"
min_silence_len = 500 # milliseconds
silence_threshold = -25

