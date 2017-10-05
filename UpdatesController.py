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

from aux import iprint
from aux import DEBUG
from aux import set_log as log



firebase = pyrebase.initialize_app(auth.config())
db = firebase.database()



def stream_handler(message):
	#TODO: Crear un hilo por cada fichero editado recibido para mejorar el rendimiento
	print(message)
	try:
		print("TEXT: "+ str(message["data"]["text"]))
	except Exception as e:
		a = 0
	try:
		print("TIMESTAMP: "+ str(message["data"]["timestamp"]))	
	except Exception as e:
		a = 0
	




class UpdatesController:

	def __init__(self, project, user_id):
		
		self.project = project
		self.user_id = user_id
		self.stream = None


	def receive_updates(self):
		global db

		print("thread working in stream: "+str(self.project)+" and user_id: "+str(self.user_id))
		self.stream = db.child(self.project).stream(stream_handler)

	def stop_updates(self):
		self.stream.close()

