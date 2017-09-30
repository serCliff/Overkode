#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff

# FUTURE: Method of use of firebase
# firebase = pyrebase.initialize_app(auth.config())
# db = firebase.database()
# db.child("users").set(data) ## To save data with a unique, auto-generated, timestamp-based key, use the push() method.
# db.child("users").push(data) ## To create your own keys use the set() method. The key in the example below is "Morty".
# db.child("users").update(data) ## To update data for an existing entry use the update() method.
# db.child("users").remove(data) ## To delete data for an existing entry use the remove() method.

# user = db.child("users").get().key() ## Calling key() returns the key for the query data.
# user = db.child("users").get().val() ## Queries return a PyreResponse object. Calling val() on these objects returns the query data.
# all_users = db.child("users").get().each() ## Returns a list of objects on each of which you can call val() and key().
# for user in all_users:
#     print(user.key()) # Morty
#     print(user.val()) # {name": "Mortimer 'Morty' Smith"}

# user = db.child("users").get() ## To return data from a path simply call the get() method.


import auth
import pyrebase
import time
import hashlib
from aux import iprint
from aux import DEBUG
from aux import set_log as log


firebase = pyrebase.initialize_app(auth.config())
db = firebase.database()





def create_random_link():
	#TODO: create_random_link
	"""
	Create Random Link: Returns a link avaiable to your project
		return: new link of project 
		
		# 1 Crear un link
		# 2 Comprobar que no existe ninguno igual
		# 	2.1 Si existe uno igual, volver a paso 1
		# 	2.2 Si el link es único continuar
		# 3 Devolver link 

	"""

	global db

	iprint (DEBUG.PRINT, "something")

def save_project(owner, data):
	""" SAVE PROJECT """

	iprint(DEBUG.WARNING, "SAVING DATA: "+ str(len(data)) +" projects")

	for project_id, project in data.items():
		
		set_project_info(project_id, project['project'])

		for user_id, user_data in project['users'].items():
			set_collaborator(project_id, user_data)

		for file_name, files in project['files'].items():
			set_files(project_id, files)
		
		for file_name, file_data in project['file_data'].items():
			for row, info in file_data.items():
				set_file_data(project_id, file_name, row, info)
		
	iprint(DEBUG.WARNING, "SAVED")


def set_project_info(project_id, project):
	""" Save Project Info """
	global db
	try:
		db.child(project_id).child("project").set(project)
	except Exception as e:
		iprint(DEBUG.ERROR, "[set_project_info]: Throw errors, exception: "+ str(e))


def set_files(project_id, files):
	""" Save Files Info of Project """
	global db
	try:
		db.child(project_id).child("files").child(hashlib.md5(str(files['name'])).hexdigest()).set(files)
	except Exception as e:
		iprint(DEBUG.ERROR, "[set_files]: Throw errors, exception: "+ str(e))


def set_file_data(project_id, file_name, row, row_data):
	""" Save row of file """
	global db
	try:
		db.child(project_id).child("file_data").child(hashlib.md5(str(file_name)).hexdigest()).child(row).set(row_data)
	except Exception as e:
		iprint(DEBUG.ERROR, "[set_file_data]: Throw errors, exception: "+ str(e))


def set_collaborator(project_id, user_data):
	""" Save new collaborator of project """
	global db
	try:
		db.child(project_id).child("users").child(user_data['user_id']).set(user_data)
	except Exception as e:
		iprint(DEBUG.ERROR, "[set_collaborator]: Throw errors, exception: "+ str(e))


def delete_project(project_id):
	""" DELETE PROJECT """
	global db
	try:
		iprint (DEBUG.WARNING, "DELETING PROJECT ID ("+str(project_id)+")")
		db.remove(project_id)
		iprint (DEBUG.WARNING, "REMOVED")
	except Exception as e:
		iprint(DEBUG.ERROR, "[set_collaborator]: Throw errors, exception: "+ str(e))


def return_project(project_id):
	""" RETURN THE PROJECT IF EXISTS 
		-> Return a dict with all elements of project
	"""
	try:
		iprint (DEBUG.WARNING, "REQUEST OF PROJECT ("+str(project_id)+")")
		return db.child(project_id).get()
	except Exception as e:
		iprint(DEBUG.ERROR, "[return_project]: Throw errors, exception: "+ str(e))


def update_project(project_id, data):
	#TODO: update_project
	iprint (DEBUG.PRINT, "something")

def set_permissions(project_id, permissions):
	#TODO: set_permissions
	iprint (DEBUG.PRINT, "something")

def return_collaborators(project_id):
	#TODO: return_collaborators
	iprint (DEBUG.PRINT, "something")

