class DataStore(object):
	def __init__(self):
		self.customers = {}
		self.offices = {}

	def add_customer(self, customer):
		if not self.customers.get(customer.id):
			self.customers[customer.id] = customer
		else:
			print("ERROR: customer id already exists")

	def add_office(self, office):
		if not self.offices.get(office.id):
			self.customers[office.id] = office
		else:
			print("ERROR: office id already exists")