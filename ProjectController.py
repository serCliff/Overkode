#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff




import auth
import pyrebase
import time
import json
import Project
import hashlib

from aux import iprint
from aux import DEBUG
from aux import set_log as log



class ProjectController:

	def __init__(owner, collaborators, project_id, data, platform):
		self.owner = owner
		self.collaborators = collaborators
		self.project_id = project_id
		self.data = data
		self.platform = platform

	def new_project(owner, platform):
		#TODO: new_project
		iprint (DEBUG.PRINT, "something")

	def selected_text(owner, permissions):
		#TODO: selected_text
		iprint (DEBUG.PRINT, "something")

	def read_current_directory():
		#TODO: read_current_directory
		iprint (DEBUG.PRINT, "something")

	def change_permissions(permissions):
		#TODO: change_permissions
		iprint (DEBUG.PRINT, "something")

	def show_project_id():
		#TODO: show_project_id
		iprint (DEBUG.PRINT, "something")

	def add_collaborator(user):
		#TODO: add_collaborator
		iprint (DEBUG.PRINT, "something")

	def file_to_project(file):
		#TODO: file_to_project
		iprint (DEBUG.PRINT, "something")


def project_to_json(project):

	""" Change project created on classes to JSON to be saved 
		-> Return a jason with all elements of project
	"""
	
	
	#TODO: project_to_json
	iprint (DEBUG.PRINT, "***************************")
	iprint (DEBUG.PRINT, "PARSE PROJECT TO JSON\n")

	projects = dict()

	for p in project:
		project_data = dict()
		project_data["id"] = p.get_project_id()
		project_data["permissions"] = p.get_permissions()
		project_data["link"] = p.get_link()
		project_data["owner_id"] = p.get_owner_id()
		
		files = dict()
		file_data = dict()
		for name, file in p.get_files().items():
			name = hashlib.md5(name).hexdigest()
			
			files[name] = dict()
			files[name]["name"] = file.get_name()
			files[name]["path"] = file.get_path()
			files[name]["permissions"] = file.get_name()

			file_data[name] = dict()
			for row, row_data in file.get_data().items():
				file_data[name][row] = dict()
				file_data[name][row]["text"] = row_data.get_text()
				file_data[name][row]["permissions"] = row_data.get_permissions()
				file_data[name][row]["timestamp"] = row_data.get_timestamp()

		users = dict()
		for user_id, user in p.get_users().items():
			users[user_id] = dict()
			users[user_id]["name"] = user.get_name()
			users[user_id]["platform"] = user.get_platform()
			users[user_id]["user_id"] = user.get_user_id()
		# iprint (DEBUG.PRINT, "")

		item = dict()
		item["project"] = project_data
		item["files"] = files
		item["file_data"] = file_data
		item["users"] = users

		projects[project_data["id"]] = item

	# iprint (DEBUG.PRINT, projects)
	returned_data = json.dumps(projects)
	data_string = json.dumps(projects, sort_keys=True, indent=4, separators=(',', ': '))
	
	iprint (DEBUG.PRINT, 'JSON:'+ str(data_string))

	return returned_data

