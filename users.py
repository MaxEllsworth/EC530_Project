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
	user = type(user_type, (user_metaclass,),traits)
	print(user.__name__)

def type_fixer(field, out_type):
	out = None
	if (out_type == "str"):
		out = str(field)
	if (out_type == "int"):
		try:
			out = int(field)
		except TypeError:
			pass
	if (out_type == "float"):
		try:
			out = float(field)
		except TypeError:
			pass
	return out

def field_merger(schema, data):
	# recursively merge fields
	True
if __name__ == "__main__":
	add_user("doctor", {})