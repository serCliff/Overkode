#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff




import auth
import pyrebase
import time
import json
import Project



class ProjectController:

	def __init__(owner, collaborators, project_id, data, platform):
		self.owner = owner
		self.collaborators = collaborators
		self.project_id = project_id
		self.data = data
		self.platform = platform

	def new_project(owner, platform):
		#TODO: new_project
		print ("something")

	def selected_text(owner, permissions):
		#TODO: selected_text
		print ("something")

	def read_current_directory():
		#TODO: read_current_directory
		print ("something")

	def change_permissions(permissions):
		#TODO: change_permissions
		print ("something")

	def show_project_id():
		#TODO: show_project_id
		print ("something")

	def add_collaborator(user):
		#TODO: add_collaborator
		print ("something")

	def project_to_json(project):
		#TODO: project_to_json
		print ("something")
		users = dict()
		for user_id, user in project.get_users().items():
			users[user_id] = dict()
			users[user_id]["name"] = user.get_name()
			users[user_id]["platform"] = user.get_platform()
			users[user_id]["user_id"] = user.get_user_id()

		print user_id



	def file_to_project(file):
		#TODO: file_to_project
		print ("something")

