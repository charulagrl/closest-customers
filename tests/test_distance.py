# -*- coding: utf-8 -*-

import pytest
from closest_customers.models import location, customer, office
from closest_customers.controller import distance
from closest_customers.store import data_store
from closest_customers.config import Staging

class TestDistanceMethods():

	def setup(self):
		self.customer_location = location.Location(53.339428, -6.257664)
		self.office_location = location.Location(53.459428, -7.257664)
		self.customer = customer.Customer(1, "Charul", self.customer_location)
		self.office = office.Office(1, "Intercom", self.office_location)
		self.distance_obj = distance.Distance(Staging.distance_limit)

	def test_get_distance(self):
		dist_value = self.distance_obj.get_distance(self.customer_location, self.office_location)
		assert 67.62690469703962 == dist_value


	def test_calculate_distances(self):
		store = data_store.DataStore(Staging.data_file_path)
		distance_dict = self.distance_obj.calculate_distances(store, 1)
		assert {} == distance_dict
		