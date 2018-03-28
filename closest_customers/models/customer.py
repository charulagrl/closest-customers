# -*- coding: utf-8 -*-

class Customer(object):
	'''Class to represent customer'''

	def __init__(self, user_id, name, location):
		self.id = user_id
		self.name = name
		self.location = location

	def get_user_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_location(self):
		return self.location
