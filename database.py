#!/usr/bin/python3


from pymongo import MongoClient
import json, flatten_json # flatten json has to be installed
import variables
import users
mongodb_port = variables.mongodb_port
mongodb_address = variables.mongodb_address

def item_generator(json_input, lookup_key):
	# source: https://stackoverflow.com/questions/21028979/recursive-iteration-through-nested-json-for-specific-key-in-python
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)

def jsonify(object):
	return {key:value for key, value in object.__dict__.items() if not key.startswith('__') and not callable(key)}

class mongo_user_wrapper(object):
	def __init__(self, user_object = ""):
		self.user_object = user_object
	def save(self):
		j = flatten_json.flatten(jsonify(self.user_object))
		print(j)
		
		True
	def update(self):
		True
	


	
if __name__ == "__main__":
	client = MongoClient(mongodb_address, mongodb_port)
	db = client["patients"]
	patient_uuid = db["patient_uuid"]
	user = users.add_user("patient", {})
	db_wrapper = mongo_user_wrapper(user)
	db_wrapper.save()
#	print(db)
