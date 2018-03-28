# -*- coding: utf-8 -*-

import logging
import math
from closest_customers.config import Production

class Distance(object):
	'''Class to calculate distance between office and all customers'''
	def __init__(self, limit=-1):
		self.distances = {}
		self.limit = Production.distance_limit if limit < 0 else limit

	def calculate_distances(self, data_store, office_id):
		customers = data_store.get_all_customers()
		office = data_store.get_office_by_id(office_id)

		if not office:
			logging.error("Office id is invalid")
			exit()

		for customer in customers.values():
			distance = self.get_distance(customer.get_location(), office.get_location())
			if distance < self.limit:
				self.distances[customer.id] = distance

		return self.distances

	def get_distance(self, customer_loc, office_loc):
		# Calculate distance using the formula given her
		# https://en.wikipedia.org/wiki/Great-circle_distance
		long_diff = abs(customer_loc.get_radian_longitude() - office_loc.get_radian_longitude())

		sin_customer_lat = customer_loc.get_sin_latitude()
		sin_office_lat = office_loc.get_sin_latitude()

		cos_customer_lat = customer_loc.get_cos_latitude()
		cos_office_lat = office_loc.get_cos_latitude()
		cos_long_diff = math.cos(long_diff)

		delta = (sin_customer_lat * sin_office_lat) + (cos_customer_lat * cos_office_lat * cos_long_diff)

		# 6371 is radius of earth
		distance = 6371 * math.acos(delta)

		return distance
