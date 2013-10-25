# -*- coding: utf-8 -*- 

class Entidade():
        def __init__(self):
                pass

        def __str__(self):                
		attrs =vars(self)
		s= ''.join("%s: %s\n" % item for item in attrs.items())
		return s
