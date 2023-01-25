#!/usr/bin/env python3
import os
import json

if(dict(os.environ)["QUERY_STRING"] == ""):
	print("Content-type: application/json\n\n")
	print(json.dumps(dict(os.environ)))
else:
	print("Content-type: text/html\n\n")
	print("{{Query String: {}, HTTP_USER_AGENT: {}".format(dict(os.environ)["QUERY_STRING"], dict(os.environ)["HTTP_USER_AGENT"]))
	for i in dict(os.environ)["QUERY_STRING"].split("&"):
		print(", {}: {}".format(i, dict(os.environ)[i]))
	print("}}")
