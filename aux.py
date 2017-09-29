#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff


import auth
import pyrebase
from enum import Enum
from random import randint
import hashlib


log = 1

def iprint(text):
	global log
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

