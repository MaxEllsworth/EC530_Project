#/usr/bin/python3
import template
import variable
'''
Types of users:
	patients
	doctors
	administrators
'''

class user_metaclass(type):
	def __new__(class_name, what, bases=None, dict=None):
		return type.__new__(class_name,what,bases,dict)


def add_user(user_type): 
	True



if __name__ == "__main__":
	template.load_template("patient")	