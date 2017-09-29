#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff

import auth
import pyrebase


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


	# data = [{"name": "Mortimer 'Morty' Smith", "auth": "asdasdasdas"}, {"name": "'Morty' Smith", "auth": "asdasdasdas"}, {"name": "Mortimer 'Morty'", "auth": "asdasdasdas"}]
	# db.child("users").child("Morty").set(data)


	# user = db.child("users").get()

	# val = user.val().popitem()
	# print(val) # users
	# print(val[0]) # users
	# print(val[1]) # users
	# print(val[1][0]["name"]) # users
	# print(val[1][1]["name"]) # users



	my_stream = db.child("users").stream(stream_handler)



if __name__ == '__main__':
    main()
