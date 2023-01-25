#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import secret as s
import templates as t
import http.cookies as c
import os

# Python 3.7 versus Python 3.8
try:
    from cgi import escape #v3.7
except:
    from html import escape #v3.8

cookie = c.SimpleCookie(os.environ["HTTP_COOKIE"])
username_c = None
password_c = None
if(cookie.get("username") and cookie.get("password")):
	username_c = cookie.get("username").value
	password_c = cookie.get("password").value
fields = cgi.FieldStorage()
username = fields.getvalue("username")
password = fields.getvalue("password")

if((username !=s.username or password != s.password) and (s.username != username_c or s.password != password_c)):
	print(t.login_page())
elif((username == s.username and password == s.password) or (s.username == username_c or s.password == password_c)):
	if((username == s.username and password == s.password) and (s.username != username_c or s.password != password_c)):
		print("Set-Cookie: username={}".format(username))
		print("Set-Cookie: password={}".format(password))
	print("Content-type: text/html\n\n")
	print(t.secret_page(s.username, s.password))
else:
	print(t.login_page())
