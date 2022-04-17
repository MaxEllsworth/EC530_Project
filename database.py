#!/usr/bin/python3


from pymongo import MongoClient
import json
import variables
import users
mongodb_port = variables.mongodb_port
mongodb_address = variables.mongodb_address

class mongo_user_wrapper(object):
	def __init__(self, user_object = ""):
		self.user_object = user_object
	def save(self):
		print(self.user_object.__dict__)
		True
	def update(self):
		True
	


	
if __name__ == "__main__":
	client = MongoClient(mongodb_address, mongodb_port)
	db = client["patients"]
	patient_uuid = db["patient_uuid"]
	user = users.add_user("doctor", {})
	db_wrapper = mongo_user_wrapper(user)
	db_wrapper.save()
	print(db)
