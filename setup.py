#!/usr/bin/env python

from distutils.core import setup

setup(
	name="BookStore",
	version="1.0",
	description="BookStore - Flask app",
	author="Benjamin Casey-Fletcher",
	author_email="benjicf97@gmail.com",
	url="",
	packages=["app", "app.routes", "app.services"],
	install_requires=[
		"flask",
		"pymongo",
		"httplib2",
		"oauth2client",
		"google-api-python-client"
	]
)
