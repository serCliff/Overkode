#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff

import auth
import pyrebase
import sys
import json
import Test
import Project
import ProjectController
import ProjectController as pr
import DataController
from aux import iprint
from aux import DEBUG
from aux import set_log as log




firebase = pyrebase.initialize_app(auth.config())
db = firebase.database()



def stream_handler(message):
	iprint (DEBUG.WARNING, message)


def main():

	if sys.argv[len(sys.argv)-1] == "debug":
		log(0)

	global db


	# ## MAKE RANDOM DATA
	# for project in Test.test_data():
	# 	data = ProjectController.project_to_json(project)
	# 	DataController.update_project(data)



	# ## TEST SAVE DIFFERENT DATA
	# data = json.loads(json.dumps({"permissions": 2,"text": "Primera linea editada y comprobada","timestamp": "00/00/0000"}))
	# DataController.set_file_data("2994bf18db049b860b87943cd21b978c", "c672c18b046f9c4be7f33e39f62bb942", "1", data)
	# for i in range(0,100):
	# 	data = json.loads(json.dumps({"permissions": 2,"text": "Primera linea editada y comprobada "+str(i)+" veces","timestamp": "00/00/0000"}))
	# 	DataController.set_file_data("2994bf18db049b860b87943cd21b978c", "c672c18b046f9c4be7f33e39f62bb942", "1", data)

	# ## TEST RETRIEVE DATA OF PROJECT
	# data = DataController.return_project("2994bf18db049b860b87943cd21b978c")
	# print data.val()

	# ## TEST RETRIEVE COLLABORATORS OF PROJECT
	# data = DataController.return_collaborators("2994bf18db049b860b87943cd21b978c")
	# print (data.val())

	# ## TEST UPDATE DATA OF SOME PROJECT
	# data = json.loads(json.dumps({"2994bf18db049b860b87943cd21b978c": {"file_data": {"c672c18b046f9c4be7f33e39f62bb942": {"20": {"permissions": 1,"text": "TEST UPDATE DATA","timestamp": "00/00/0000"}}}}}))
	# DataController.update_project(data)

	## TEST CREATING NEW PROJECT
	owner_id = "sercliff_id"
	link = "htt://sergiodelcastillo.com/"+owner_id
	project_id = "pruebaProyecto"
	data = "data"
	platform = "sublime"	
	scope = dict()
	# scope['range'] = "project"
	scope['range'] = "file"
	scope['path'] = "/home/sergiodebian/Overkode/Test.py"

	permissions = Project.Project_Permissions.FULL

	collaborators = dict()
	collaborators[owner_id] = Project.User(owner_id, "sercliff", platform)
	pro = pr.ProjectController(owner_id, collaborators, project_id, link, platform)

	pro.new_project(scope, permissions)


	# ## TEST create_project_rowInfo()
	# permissions = dict()
	# for i in range(80, 101):
	# 	permissions[i] = Project.Permissions.WRITE.value

	# value = pc.create_project_rowInfo("/home/sergiodebian/Overkode/Test.py", permissions)
	
	# for row, rowinfo in value.items():
	# 	print("["+str(row) + " : "+str(rowinfo.permissions)+"] " + str(rowinfo.text))

	# ## STREAM
	# my_stream = db.child("2994bf18db049b860b87943cd21b978c").stream(stream_handler)

	# my_stream.close()



if __name__ == '__main__':
    main()



















