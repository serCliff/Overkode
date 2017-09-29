#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff

import auth
import pyrebase
import json
import Project as pro
from random import randint
import hashlib



def test_data():
	
	project = list()

	for i in xrange(0, randint(1, 4)):
		num_files = randint(1, 5)
		num_users = randint(1, 5)
		
		p = pro.Project(hashlib.md5().hexdigest(), "sercliff", num_files, num_users)
		project.append(p)

	print ("\nPROJECT\n------------------")

	for p in project:
		print ("Project_id: "+str(p.get_project_id()))
		print ("Owner: "+str(p.get_owner_id()))
		print ("\n**** USERS ****")
		for k, user in p.get_users().items():
			print ("User_id: "+str(k))
			print ("Name: "+str(user.get_name()))
			print ("Platform: "+str(user.get_platform()))
			print("")
		print ("\n**** FILES *****")
		for k, file in p.get_files().items():
			print ("\nFILE: "+str(k))
			print ("Path: "+str(file.get_path()))
			for row, data in file.get_data().items():
				print (str(row)+" - "+data.get_text())	
		print ("\n------------------\n")


	print ("FINALIZADO")
	return project


def main():

	project = test_data()


	users = dict()
	for user_id, user in project.get_users().items():
		users[user_id] = dict()
		users[user_id]["name"] = user.get_name()
		users[user_id]["platform"] = user.get_platform()
		users[user_id]["user_id"] = user.get_user_id()

	print user_id



if __name__ == '__main__':
    main()
