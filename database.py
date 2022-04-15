#!.python_venv/bin/python3.8

mongodb_port = 27017
mongodb_address = "localhost"
from pymongo import MongoClient
import json


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
