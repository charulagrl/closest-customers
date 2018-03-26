class Office(object):
	def __init__(self, office_id, name, latitude, longitude):
		self.id = office_id
		self.name = name
		self.latitude = latitude
		self.longitude = longitude

	def get_user_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_latitude(self):
		return self.latitude

	def get_longitude(self):
		return self.longitude
