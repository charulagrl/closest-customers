from location import Location

class Office(object):
	'''Class to represent office'''

	def __init__(self, office_id, name, latitude, longitude):
		self.id = office_id
		self.name = name
		self.location = Location(latitude, longitude)

	def get_user_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_location(self):
		return self.location
