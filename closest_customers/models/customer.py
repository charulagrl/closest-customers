from location import Location

class Customer(object):
	'''Class to represent customer'''

	def __init__(self, user_id, name, latitude, longitude):
		self.id = user_id
		self.name = name
		self.location = Location(latitude, longitude)

	def get_user_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_location(self):
		return self.location
