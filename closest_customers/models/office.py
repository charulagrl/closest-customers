class Office(object):
	'''Class to represent office'''

	def __init__(self, office_id, name, location):
		self.id = office_id
		self.name = name
		# location can be an array also
		self.location = location

	def get_user_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_location(self):
		return self.location
