#!/usr/bin/python3
#https://medium.com/fintechexplained/advanced-python-metaprogramming-980da1be0c7d#:~:text=Python%20uses%20a%20metaclass%20to,special%20behavior%20to%20a%20class.
# https://www.geeksforgeeks.org/read-json-file-using-python/
#https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence

from flask_restx import Resource, Namespace, Api
from flask import Flask, Blueprint
import logging
import json
import pickle
import variables
import os

device_templates = variables.device_templates

device_namespace = Namespace('device', 'Device Methods')

device_blueprint = Blueprint("Device blueprint", __name__)

class device_metaclass(type):
	def __new__(class_name, what, bases=None, dict=None):
		return type.__new__(class_name,what,bases,dict)


app = Flask(__name__)
#api = Api(app)

#@app.route('/instantiate_device')
#def instantiate_device(device_name):
@device_blueprint.route("/list_devices")
def list_devices():
#	f = open(device_templates + "devices.json")
#	devices = json.load(f)
#	f.close()
	
	all_device_info = {}
	devices = [dev.rstrip(".json") for dev in os.listdir(device_templates) if ".json" in dev]
	print(devices)
	for device_name in devices:
		f = open(device_templates + device_name + ".json")
		device_info = json.load(f)#devices["devices"][dev]
		f.close()
		device = type("device",(device_metaclass,), device_info)
		all_device_info.update(device_info)
	#	with open(device_templates + device_name + ".pkl","wb") as output:
	#		pickle.dump(device[device_name], output, pickle.HIGHEST_PROTOCOL)
	#	#class_keys = 
	return all_device_info


if __name__ == "__main__":
	list_devices()