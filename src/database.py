#!/usr/bin/python3


from pymongo import MongoClient
from flask import Flask, Blueprint
import json, flatten_json # flatten json has to be installed
import variables
import users
from time import sleep, time

mongodb_port = variables.mongodb_port
mongodb_address = variables.mongodb_address
mongodb_uri = variables.mongodb_uri

app = Flask(__name__)
db_blueprint = Blueprint("Database blueprint", __name__)


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
		self.client = MongoClient(mongodb_uri)
	
	def show(self):
		collection_name = self.user_object.__name__
		db = self.client[collection_name]
		col = db["fake uid"]
		cursor = col.find({})
		for document in cursor:
			print(document)
	def save(self, uid = "1234"):
		flattened = flatten_json.flatten(jsonify(self.user_object))
		collection_name = self.user_object.__name__
		flattened['cao'] = float(time())		
		columns = flattened.keys() 
		db = self.client[collection_name]
		col = db[uid]
		col.insert_one(flattened)
	
	def uid_available(self, uid = ""):
		collection_name = self.user_object.__name__
		db = self.client[collection_name]
	#	col = db["fake uid"]
    #    if (uid == None) or (type(uid) != str):
    #        uid = uuid.uuid4().hex
		return True


			
		#print(db.list_collection_names())

#@db_blueprint.route("/user/",methods=["POST"])

'''def mongo_user_web_wrapper(action = "", collection_name = "",attributes={}):
	client = MongoClient(mongodb_uri)
	user = users.add_user(collection_name, attributes)
	db_wrapper = mongo_user_wrapper(user)
	if (action == "save"):
		db_wrapper.save()
	if (action == "show"):
		db_wrapper.show()
'''

	#	for col in columns:
	#		print("column is " + col)
	#	#	if col not in db.list_collection_names():
	#		inserted_column = db[col]
	#		inserted_content = flattened[col]
	#		print(type(inserted_content))
	#		if (inserted_content != None):
	#			#inserted_content = {}
	#			print("content is as follows " + str(inserted_content))
	#			inserted_column.insert_one(inserted_content)
	#		

	#	True
	#def update(self):
#		True
	


	
if __name__ == "__main__":
	print(mongodb_uri)

#	db = client["patients"]
#	column = db["test_column"]
#	test_dict = {"1" : "one", "2" : "two"}
#	column.insert_one(test_dict)
#	print("Collection names are as follows:")
#	print(db.list_collection_names())
#	patient_uuid = db["patient_uuid"]

