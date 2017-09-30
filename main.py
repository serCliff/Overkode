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

	# firebase = pyrebase.initialize_app(auth.config())
	# db = firebase.database()

	## Make random data
	# data = ProjectController.project_to_json(Test.test_data())
	# ## decode the data
	# decoded = json.loads(data)
 	# ## Save random data
	# DataController.save_project("owner", decoded)


	## TEST SAVE DIFFERENT DATA
	# data = json.loads(json.dumps({"permissions": 2,"text": "Primera linea editada y comprobada","timestamp": "00/00/0000"}))
	# DataController.set_file_data("682564f311338a716aa8f5ce4db51590", "eccbc87e4b5ce2fe28308fd9f2a7baf3.py", "1", data)
	# for i in xrange(0,5):
	# 	data = json.loads(json.dumps({"permissions": 2,"text": "Primera linea editada y comprobada "+str(i)+" veces","timestamp": "00/00/0000"}))
	# 	DataController.set_file_data("682564f311338a716aa8f5ce4db51590", "eccbc87e4b5ce2fe28308fd9f2a7baf3.py", "1", data)

	## TEST RETRIEVE DATA OF PROJECT
	# data = DataController.return_project("682564f311338a716aa8f5ce4db51590")
	# print data.val()


	## STREAM
	# my_stream = db.child("users").stream(stream_handler)



if __name__ == '__main__':
    main()



















