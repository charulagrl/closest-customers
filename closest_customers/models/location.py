from utils.maths_conversions import MathsConversions
import math

class Location(object):
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def get_radian_location(self):
		return (math.radians(self.latitude), math.radians(self.longitude))

	def get_radian_latitude(self):
		return math.radians(self.latitude)

	def get_radian_longitude(self):
		return math.radians(self.longitude)

	def get_sin_latitude(self):
		latitude = math.radians(self.latitude)
		return math.sin(latitude)

	def get_cos_latitude(self):
		latitude = math.radians(self.latitude)
		return math.cos(latitude)