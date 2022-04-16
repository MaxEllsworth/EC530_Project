#!/usr/bin/python3
import template
import variables
'''
Types of users:
	patients
	doctors
	administrators
'''

class user_metaclass(type):
	def __new__(class_name, what, bases=None, dict=None):
		return type.__new__(class_name,what,bases,dict)

def add_user(user_type, user_info, uid = ""): 
	traits = template.load_template(user_type)
	user = type("user", (user_metaclass,),traits)
	print(user.identity)

def type_fixer(field, out_type):
	out = None
	if (out_type == "str"):
		out = str(field)
	if (out_type == "int"):
		try:
			out = int(field)
	if (out_type == "float"):
		try:
			out = float(field)
	return out
def field_merger(schema, data):
	True

if __name__ == "__main__":
	add_user("patient")