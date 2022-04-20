#!.python_venv/bin/python3
#https://medium.com/fintechexplained/advanced-python-metaprogramming-980da1be0c7d#:~:text=Python%20uses%20a%20metaclass%20to,special%20behavior%20to%20a%20class.
# https://www.geeksforgeeks.org/read-json-file-using-python/
#https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence

from flask_restx import Resource, Namespace, Api
from flask import Flask
import logging
import json
import pickle
import variables

device_templates = variables.device_templates

device_namespace = Namespace('device', 'Device Methods')

class device_metaclass(type):
	def __new__(class_name, what, bases=None, dict=None):
		return type.__new__(class_name,what,bases,dict)


app = Flask(__name__)
#api = Api(app)

@app.route('/instantiate_device')
#def instantiate_device(device_name):
def instantiate_device():
	f = open(device_templates + "devices.json")
	devices = json.load(f)
	f.close()
	

	for dev in devices["devices"]:
		device_name = dev
		device_sensors = devices["devices"][dev]

		device = type("device",(device_metaclass,), device_sensors)
		#print(device.__dict__)
		print("\n\n")
		#help(device)
		
		print(device.sensors)
		with open(device_templates + device_name + ".pkl","wb") as output:
			pickle.dump(device, output, pickle.HIGHEST_PROTOCOL)
		#class_keys = 
		return {"instantiated" : "true"}

if __name__ == "__main__":
	True