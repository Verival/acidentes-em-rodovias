#!/usr/bin/python
#-*- encoding: utf-8 -*-

import csv, sys

def parser(filename):
	with open(filename, 'rb') as filename:
	    reader = csv.reader(filename, delimiter = ';', quotechar = '"')
	    try:
	        for row in reader:
	        	print row[0] + "\t" + row[1]

	    except csv.Error as e:
	        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))



filename = "estadofisico.csv"
parser(filename)
