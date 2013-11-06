from ExceptionsDao import *

try:
	raise InvalidChar('Testando')
except InvalidChar as e:
	print e.Errors
else:
	pass
finally:
	pass