#!/usr/bin/python
#-*- encoding: utf-8 -*-

import csv, sys
import odict

class parser(object):
	data={}
	"""
	@package Parser
	construtor das informações adquiridas através do arquivo CSV.
	
	"""
	def __init__(self,filename):
		with open(filename, 'rb') as filename:
			reader = csv.reader(filename, delimiter = ';', quotechar = '\"')
			try:
				self.data=odict.odict()
				for i in reader.next():
					self.data[str(i)] = []
				for row in reader:
					for (i,d) in zip(xrange(len(row)),self.data.keys()):
						self.data[d].append(row[i])
			except csv.Error as e:
				sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
			
			self.data=dict(self.data)
			

if __name__ == "__main__":
	filename = "estadofisico.csv"
	estado_fisico=parser(filename)
	print estado_fisico.data

	Pessoa = parser("tabelaPessoa.csv")

	print Pessoa.data.keys()
