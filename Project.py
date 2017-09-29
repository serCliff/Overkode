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
	def __init__(self, project_id, owner_id, num_files, num_users):
		owner_id = str(owner_id)
		self.project_id = project_id
		self.permissions = randint(1, 4)
		self.link = "http://sergiodelcastillo.com/"+owner_id
		self.owner_id = owner_id
		self.files = dict()
		self.users = dict()
		
		user_id = hashlib.md5(owner_id).hexdigest()
		u = User(user_id, owner_id, "sublime")
		self.users[user_id] = u

		for user in xrange(1, num_users):
			user_id = hashlib.md5(str(user)).hexdigest()
			user = "sercliff_"+str(user)
			u = User(user_id, user, "sublime")
			self.users[user_id] = u

		for file in xrange(1, num_files):
			data = dict()

			for row in xrange(1,20):
				text = hashlib.sha384(str(row*file)).hexdigest()
				permissions = randint(1, 3)
				timestamp = "00/00/0000"
				r = RowInfo(text,permissions,timestamp)
				data[row] = r

			name = str(hashlib.md5(str(file)).hexdigest())+".py"
			path = "/path/"+name
			permissions = randint(1, 4)
			f = Files(name, path, permissions, data)
			self.files[name] = f

	def get_project_id(self):
		return self.project_id
	def get_permissions(self):
		return self.permissions
	def get_link(self):
		return self.link
	def get_owner_id(self):
		return self.owner_id
	def get_files(self):
		return self.files
	def get_users(self):
		return self.users

class Files:
	def __init__(self, name, path, permissions, data):
		self.name = name
		self.path = path
		self.permissions = permissions
		self.data = data

	def get_name(self):
		return self.name
	def get_path(self):
		return self.path
	def get_permissions(self):
		return self.permissions
	def get_data(self):
		return self.data

class RowInfo:
	def __init__(self, text, permissions, timestamp):
		self.text = text
		self.permissions = permissions
		self.timestamp = timestamp

	def get_text(self):
		return self.text
	def get_permissions(self):
		return self.permissions
	def get_timestamp(self):
		return self.timestamp

class User:
	def __init__(self, user_id, name, platform):
		self.user_id = user_id
		self.name = name
		self.platform = platform

	def get_user_id(self):
		return self.user_id
	def get_name(self):
		return self.name
	def get_platform(self):
		return self.platform












