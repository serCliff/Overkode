#!/usr/bin/env python
# -*- coding: utf-8 -*-

## SERGIO DEL CASTILLO t.me/sercliff

import auth
import pyrebase
import json
import Project as pro
from random import randint
import hashlib
from aux import iprint





def test_data():
	
	project = list()

	for i in xrange(1, randint(2, 4)):
		num_files = randint(2, 5)
		num_users = randint(1, 5)
		
		p = pro.Project(hashlib.md5(str(i)).hexdigest(), "sercliff", num_files, num_users)
		project.append(p)

	iprint ("\nPROJECT\n------------------")

	for p in project:
		iprint ("Project_id: "+str(p.get_project_id()))
		iprint ("Owner: "+str(p.get_owner_id()))
		iprint ("\n**** USERS ****")
		for k, user in p.get_users().items():
			iprint ("User_id: "+str(k))
			iprint ("Name: "+str(user.get_name()))
			iprint ("Platform: "+str(user.get_platform()))
			iprint("--")
		iprint ("\n**** FILES *****")
		for k, file in p.get_files().items():
			iprint ("\nFILE: "+str(k))
			iprint ("Path: "+str(file.get_path()))
			for row, data in file.get_data().items():
				iprint (str(row)+" - "+data.get_text())	
		iprint ("\n------------------\n")


	iprint ("FINALIZADO\n\n")
	return project


def main():

	project = test_data()

	print ("PRINTING DATA")

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
		print ("")

		item = dict()
		item["project"] = project_data
		item["files"] = files
		item["file_data"] = file_data
		item["users"] = users

		projects[project_data["id"]] = item


	data_string = json.dumps(projects, sort_keys=True, indent=4, separators=(',', ': '))
	print("")
	print 'JSON:', data_string



if __name__ == '__main__':
    main()
