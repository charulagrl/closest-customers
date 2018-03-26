from models import customer, location
from utils.maths_conversions import MathsConversions
import json

class DataLoader(object):
	'''Loads and reads raw data from file and convert it to data objects'''
	def __init__(self, data_store):
		self.path = None
		self.customers = None
		self.data_store = data_store

	def load_json_data(self):
		with open('customers.json') as data_file:
			data = json.load(data_file)

			self.customers = data["customers"]

		self.create_customer_data()

	def create_customer_data(self):
		for customer in self.customers:
			latitude = customer["latitude"]
			longitude = customer["longitude"]
			name = customer["name"]
			user_id = customer["user_id"]

			self.create_customer(user_id, name, latitude, longitude)

	def create_customer(self, user_id, name, latitude, longitude):
		latitude = MathsConversions.get_radian(float(latitude))
		longitude = MathsConversions.get_radian(float(longitude))

		new_customer = customer.Customer(user_id, name, latitude, longitude)

		self.data_store.add_customer(new_customer)

