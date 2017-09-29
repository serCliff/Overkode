#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff

import auth
import pyrebase
import json
import Test
import Project
import ProjectController
from aux import iprint


def stream_handler(message):

	print message
	# print(message[1])
	# print(message[1][0]["name"])
	# print(message[1][1]["name"])

	# val = message.val().popitem()
	# print(val) # users
	# print(val[0]) # users
	# print(val[1]) # users
	# print(val[1][0]["name"]) # users
	# print(val[1][1]["name"]) # users





def main():


	firebase = pyrebase.initialize_app(auth.config())

	db = firebase.database()


	data = ProjectController.project_to_json(Test.test_data())
	print ""
	# print data
	decoded = json.loads(data)
#TODO: Crear metodo que guarde todo correctamente en la base de datos
	for k, v in decoded.items():
		print k
		print v
		print 
	# db.set(data)
	# data = [{"name": "Mortimer 'Morty' Smith", "auth": "asdasdasdas"}, {"name": "'Morty' Smith", "auth": "asdasdasdas"}, {"name": "Mortimer 'Morty'", "auth": "asdasdasdas"}]
	# db.child("users").child("Morty").set(data)


	# user = db.child("users").get()

	# val = user.val().popitem()
	# print(val) # users
	# print(val[0]) # users
	# print(val[1]) # users
	# print(val[1][0]["name"]) # users
	# print(val[1][1]["name"]) # users



	# my_stream = db.child("users").stream(stream_handler)



if __name__ == '__main__':
    main()
