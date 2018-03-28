# -*- coding: utf-8 -*-

from .data_loader import DataLoader

class DataStore(object):
	def __init__(self, path):
		self.data_loader = DataLoader(path)
		self.customers = self.data_loader.get_customer_objects()
		self.offices = self.data_loader.get_office_objects()

	def get_all_customers(self):
		return self.customers

	def get_all_offices(self):
		return self.offices

	def get_office_by_id(self, id):
		return self.offices.get(id, None)

	def get_customer_by_id(self, id):
		return self.customers.get(id, None)
