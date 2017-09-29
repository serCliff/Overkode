#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff




import auth
import pyrebase
import time



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

	firebase = pyrebase.initialize_app(auth.config())
	db = firebase.database()

	


	print ("something")

def save_project(owner, data):
	#TODO: save_project
	print ("something")

def update_project(project_id, data):
	#TODO: update_project
	print ("something")

def delete_project(project_id):
	#TODO: delete_project
	print ("something")

def set_collaborator(user, project_id):
	#TODO: set_collaborator
	print ("something")

def set_permissions(project_id, permissions):
	#TODO: set_permissions
	print ("something")

def return_project(project_id):
	#TODO: return_project
	print ("something")

def return_collaborators(project_id):
	#TODO: return_collaborators
	print ("something")

