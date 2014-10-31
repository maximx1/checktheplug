import web
import json
import random

class TestController:

	"""
		The main get endpoint for getting the key to validate system up.
	"""
	def GET(self):
		key = {"key": random.randint(100000, 999999)}
		web.header('Content-Type', 'application/json')
		return json.dumps(key)
