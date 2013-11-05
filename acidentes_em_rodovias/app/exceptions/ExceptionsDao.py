from exceptions import Exception
from MySQLdb import DatabaseError

class ValidateDate(Exception):
	"""docstring for ValidateDate"""
	def __init__(self, message):
		Exception.__init__(self)
		self.Errors = "Data invalida"


class InvalidChar(DatabaseError):
	"""docstring for ValidateDate"""
	def __init__(self, message):
		Exception.__init__(self)
		self.Errors = "Invalid char used on search"