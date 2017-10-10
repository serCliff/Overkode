#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff



import auth
import pyrebase
import time
import json
import Project
import hashlib
import os
import glob
import threading


import DataController as dc

from aux import d2j
from aux import iprint
from aux import DEBUG
from aux import set_log as log



firebase = pyrebase.initialize_app(auth.config())
db = firebase.database()



def stream_handler(message):
	#TODO: Crear un hilo por cada fichero editado recibido para mejorar el rendimiento
	#TODO: Evitar actualizaciones que realice el propio usuario
	
	project_id = str(message["stream_id"])
	try:
		update = dict()
		update[project_id] = recursive_structure(str(message["path"]), message["data"])
		print(update)
		#TODO: Crear sistema para representar la información en el editor

	except Exception as e:
		a = 0
	

def recursive_structure(path_data, data):
	""" Make recursively the project data """
	
	key = os.path.basename(path_data)
	
	new_data = dict()
	new_data[key] = data

	new_path = path_data.replace("/"+str(key), "")
	
	if new_path == "" or path_data == "/":
		return new_data
	else:
		return recursive_structure(new_path, new_data)
	


class UpdatesController:

	def __init__(self, project, user_id):
		self.project = project
		self.user_id = user_id
		self.stream = None


	def receive_updates(self):
		global db

		print("thread working in stream: "+str(self.project)+" and user_id: "+str(self.user_id))
		self.stream = db.child(self.project).stream(stream_handler, stream_id=self.project)

	def stop_updates(self):
		self.stream.close()









