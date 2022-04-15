#!/usr/bin/python3


from pymongo import MongoClient
import json
import variables

mongodb_port = variables.mongodb_port
mongodb_address = variables.mongodb_address

class mongo_wrapper(object):
	def __init__(self):
		True
	def add_user(self):
		True
	def update_user(self):
		True
	


	
if __name__ == "__main__":
	client = MongoClient(mongodb_address, mongodb_port)
	db = client.users
	print(db)
