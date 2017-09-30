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
import DataController
from aux import iprint
from aux import DEBUG
from aux import set_log as log


def stream_handler(message):
	print message





def main():

	if sys.argv[len(sys.argv)-1] == "debug":
		log(0)

	firebase = pyrebase.initialize_app(auth.config())

	db = firebase.database()

	## Make random data
	data = ProjectController.project_to_json(Test.test_data())

	## decode the data
	decoded = json.loads(data)
 	
 	## Save random data
	DataController.save_project("owner", decoded)


	# my_stream = db.child("users").stream(stream_handler)



if __name__ == '__main__':
    main()



















