#!.python_venv/bin/python3
#https://medium.com/fintechexplained/advanced-python-metaprogramming-980da1be0c7d#:~:text=Python%20uses%20a%20metaclass%20to,special%20behavior%20to%20a%20class.
# https://www.geeksforgeeks.org/read-json-file-using-python/
#https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence

import json
import pickle

dev_objects = "./device_objects/"
class device_metaclass(type):
	def __new__(class_name, what, bases=None, dict=None):
		return type.__new__(class_name,what,bases,dict)
	#def sensors():
	#	print()
	#	pass
	#def __init__(self):#self,temp = (), syst = (), diast = (), pulse = (), oxi = (), weight = (), glucose = ()):
		'''self.temp = temp
		self.syst = syst
		self.diast = diast
		self.pulse = pulse
		self.oxi = oxi
		self.weight = weight
		self.glucose = glucose()
		'''



#class smartwatch(metaclass = device_metaclass):
	True
if __name__ == "__main__":

#	print(watch)


	f = open("devices.json")
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
		with open(dev_objects + device_name + ".pkl","wb") as output:
			pickle.dump(device, output, pickle.HIGHEST_PROTOCOL)
		#class_keys = 