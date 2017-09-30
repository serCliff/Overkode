#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff


import auth
import pyrebase
from enum import Enum
from random import randint
import hashlib


class DEBUG(Enum):
	ALL = 1 
	ERROR = 2 
	WARNING = 3 
	PRINT = 4 
	NONE = 5 



log = 1


def iprint(debug, text):
	global log

	if debug == DEBUG.ERROR:
		print (decode(text))
	
	elif debug == DEBUG.WARNING:
		print (decode(text))
	
	elif debug == DEBUG.ALL:
		print (decode(text))
	
	elif debug == DEBUG.PRINT:
		if log == 0:
			print (decode(text))



def decode(text):
	
	try:
		text = unidecode(unicode(text, errors='replace'))	
	except Exception as e:
		try:
			text = unidecode(text)	
		except Exception as e:
			try:
				text = str(text.toAscii)	
			except Exception as e:
				text = str(text)


	text = text.replace("\'", "\"")
	return text


def set_log(value):
	global log
	log = value