from utils.maths_conversions import MathsConversions
import math

class Distance(object):
	def __init__(self, limit):
		self.distances = {}
		self.limit = limit

	def calculate_distances(self, data_store, office_id):
		customers = data_store.customers
		office = data_store.offices.get(office_id, None)

		if not office:
			print("Office id is invalid")
			return

		for customer in customers.values():
			distance = self.get_distance(customer.get_location(), office.get_location())
			if distance < self.limit:
				self.distances[customer.id] = distance

		print self.distances

	def get_distance(self, customer_loc, office_loc):
		# Calculate distance using the formula given her
		# https://en.wikipedia.org/wiki/Great-circle_distance
		customer_radian_loc = customer_loc.get_radian_location()
		office_radian_loc = office_loc.get_radian_location()

		long_diff = abs(customer_loc.get_radian_longitude() - office_loc.get_radian_longitude())
		print long_diff
		sin_customer_lat = customer_loc.get_sin_latitude()
		sin_office_lat = office_loc.get_sin_latitude()
		print sin_customer_lat, sin_office_lat
		cos_customer_lat = customer_loc.get_cos_latitude()
		cos_office_lat = office_loc.get_cos_latitude()
		print cos_customer_lat, cos_office_lat
		cos_long_diff = math.cos(long_diff)

		delta = (sin_customer_lat * sin_office_lat) + (cos_customer_lat * cos_office_lat * cos_long_diff)

		# 6371 is radius of earth
		distance = 6371 * math.acos(delta)

		return distance

	# def get_distance(self, latitude, longitude, office_lat, office_long):
	# 	# Calculate distance using the formula given her
	# 	# https://en.wikipedia.org/wiki/Great-circle_distance
	# 	long_diff = abs(longitude - office_long)

	# 	sin_lat = MathsConversions.get_sin(latitude)
	# 	sin_office_lat = MathsConversions.get_sin(office_lat)

	# 	cos_lat = MathsConversions.get_cos(latitude)
	# 	cos_office_lat = MathsConversions.get_cos(office_lat)

	# 	cos_long_diff = MathsConversions.get_cos(long_diff)

	# 	delta = (sin_lat * sin_office_lat) + (cos_lat * cos_office_lat * cos_long_diff)

	# 	# 6371 is radius of earth
	# 	distance = 6371 * MathsConversions.get_acos(delta)

	# 	return distance

