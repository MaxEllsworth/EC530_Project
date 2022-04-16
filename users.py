#/usr/bin/python3

class user_metaclass(type):
	def __new__(class_name, what, bases=None, dict=None):
		return type.__new__(class_name,what,bases,dict)


def add_user(): 
	True



if __name__ == "__main__":
	True	