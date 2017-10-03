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
import DataController as dc

from aux import iprint
from aux import DEBUG
from aux import set_log as log



class ProjectController:

	def __init__(self, owner_id, collaborators, project_id, link, platform):
		self.owner_id = owner_id
		self.collaborators = collaborators ## FUTURE: En colaboradores incluir en primer momento el owner(unico usuario e ir añadiendole el resto)
		self.project_id = project_id
		self.link = link
		self.platform = platform

	def new_project(self, scope, permissions):
		""" 
			MAKE A NEW PROJECT AND SAVE IN THE DATABASE 
			scope       : Determine the range of work, Project or file, and where are all
			permissions : Determine the permissions of all project (For partial sharing in selected_text() method)
			
			-> Return   : Link/id of the project 
		"""
		general_permissions = dict()

		general_permissions['general'] = Project.Permissions.READ.value  ## By default the permissions of files will be READ
		if permissions == Project.Project_Permissions.FULL:
			general_permissions['general'] = Project.Permissions.WRITE.value
		

		current_directory = os.getcwd()+"/"	

		
		if self.platform != "web":

			if 'range' in scope and scope['range'] == "project": ## We are sharing all our project
				#FUTURE: Para que solo algún archivo del proyecto se pueda editar y el resto visualizar, utilizar el método selected_text()

				all_files = glob.glob(current_directory+'**', recursive=True) ## This version return an iterator, glob.glob returns a list 
				all_files.remove(os.getcwd()+"/")
				
				iprint (DEBUG.PRINT, current_directory)

				iprint (DEBUG.PRINT, "\n|\t\tDIRECTORIES\r\t\t\t\t\t|\t\tDIRECTORY")
				for file in all_files:
					if os.path.isdir(file):
						iprint (DEBUG.PRINT, "| "+os.path.basename(file)+"\r\t\t\t\t\t| "+file.replace(current_directory, "/"))

				iprint (DEBUG.PRINT, "\n|\t\tFILE\r\t\t\t\t\t|\t\tDIRECTORY")
				for file in all_files:
					if os.path.isfile(file):
						iprint (DEBUG.PRINT, "| "+os.path.basename(file)+"\r\t\t\t\t\t| "+file.replace(current_directory, "/"))

			elif 'range' in scope and scope['range'] == "file": ## Only we will share the file with name is in scope['path']
				file = scope['path']
				name = str(os.path.basename(file))
				path = file.replace(current_directory, "/")
				
				iprint (DEBUG.PRINT, "| "+name+"\r\t\t\t\t\t| "+path)
				## MAKING FULL PROJECT WITH ONE FILE
				row_info = create_project_rowInfo(file, general_permissions)
				file = create_project_files(name, path, permissions.value, row_info)
				files = dict()
				files[name] = file


				project = create_project(self.project_id, self.link, permissions.value, self.owner_id, files, self.collaborators)
				dc.update_project(project_to_json(project))
				#TODO: CREAR SISTEMA DE ACTUALIZACIONES, asignar el nuevo proyecto creado y subirlo a la base de datos



		else: 
			iprint(DEBUG.PRINT, "With web platform create a new file of project and begin")
		# print (all_data)







def create_project(project_id, link, permissions, owner_id, files, users):
	return Project.Project(project_id, permissions, link, owner_id, files, users)


def create_project_files(name, path, permissions, data):
	iprint (DEBUG.PRINT, "CREATING PROJECT FILE INFO")
	return Project.Files(name, path, permissions, data)

def create_project_rowInfo(file_path, permissions):
	""" 
		Make a RowInfo class with the information content in the file 
		file_path   : The path of file that will be readed
		permissions : dict[row, permission] with special permissions (if is empty all rows have Permissions.WRITE) | 'general' to assign manually general permissions
		-> Return   : dict[row, RowInfo] filled with the file_path information
	"""
	iprint (DEBUG.WARNING, "CREATING PROJECT RowInfo to: "+str(file_path))

	row_info = dict()
	try:
		timestamp = "00/00/0000"
		
		if len(permissions):
			row_permissions = Project.Permissions.READ.value
		elif 'general' in permissions:
			row_permissions = permissions['general']
		else:
			row_permissions = Project.Permissions.WRITE.value
		
		with open(file_path) as file:
			row=1
			for line in file:
				row_info[row] = Project.RowInfo(line, row_permissions, timestamp)
				row+=1
		
		try:
			if not 'general' in permissions and len(permissions):
				iprint(DEBUG.PRINT, "Rewrite rows with special permissions")
				for row, permission in permissions.items():
					row_info[row].set_permissions(permission)

		except Exception as e:
			iprint(DEBUG.ERROR, "[create_project_rowInfo] : Changing File Permissions was throwed an exception: "+str(e))
	except Exception as e:
		iprint(DEBUG.ERROR, "[create_project_rowInfo] : Reading File was throwed an exception: "+str(e))


	iprint(DEBUG.WARNING, "RowInfo was done")

	return row_info



def selected_text(owner_id, permissions):
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
		-> Return a json with all elements of project
	"""
	
	
	#TODO: project_to_json
	iprint (DEBUG.PRINT, "***************************")
	iprint (DEBUG.PRINT, "PARSE PROJECT TO JSON\n")

	projects = dict()

	# for p in project:


	project_data = dict()
	project_data["id"] = project.get_project_id()
	project_data["permissions"] = project.get_permissions()
	project_data["link"] = project.get_link()
	project_data["owner_id"] = project.get_owner_id()
	
	files = dict()
	file_data = dict()
	for name, file in project.get_files().items():
		
		name = hashlib.md5(name.encode('utf-8')).hexdigest()
		
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
	for user_id, user in project.get_users().items():
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

	# return returned_data
	return json.loads(returned_data)

