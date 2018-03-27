from data_loader import DataLoader

class DataStore(object):
	def __init__(self, path):
		self.data_loader = DataLoader(path)
		self.customers = {}
		self.offices = {}

		self.add_customers()
		self.add_offices()

	def add_customers(self):
		self.customers = self.data_loader.get_customer_objects()

	def add_offices(self):
		self.offices = self.data_loader.get_office_objects()