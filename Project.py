#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff


import auth
import pyrebase
from enum import Enum
from random import randint
import hashlib


log = 0

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



class Project_Permissions(Enum):
	FULL = 1 ## Show and Write all
	ROWS = 2 ## Show all, Write only some rows
	SOME = 3 ## Show and Write only some rows
	SHOW = 4 ## Only Show all

class Permissions(Enum):
	WRITE = 1 
	READ = 2 
	NONE = 3 



class Project:

	def __init__(self, project_id, permissions, link, owner, files, users):
		self.project_id = project_id
		self.permissions = permissions
		self.link = link
		self.owner = owner
		self.files = files
		self.users = users

	## SAMPLE CREATOR ##
	def __init__(self, owner, num_files, num_users):
		self.project_id = project_id
		self.permissions = permissions
		self.link = link
		self.owner = owner
		self.files = dict()
		self.users = dict()

		for user in xrange(1, num_users):



	
	def get_project_id():
		return project_id
	def get_permissions():
		return permissions
	def get_link():
		return link
	def get_owner():
		return owner
	def get_files():
		return files
	def get_users():
		return users

class Files:
	def __init__(self, name, path, permissions, data):
		self.name = name
		self.path = path
		self.permissions = permissions
		self.data = data

	def get_name():
		return name
	def get_path():
		return path
	def get_permissions():
		return permissions
	def get_data():
		return data

class RowInfo:
	def __init__(self, text, permissions, timestamp):
		self.text = text
		self.permissions = permissions
		self.timestamp = timestamp

	def get_text():
		return text
	def get_permissions():
		return permissions
	def get_timestamp():
		return timestamp

class User:
	def __init__(self, user_id, name, platform):
		self.user_id = user_id
		self.name = name
		self.platform = platform

	def get_user_id():
		return user_id
	def get_name():
		return name
	def get_platform():
		return platform












