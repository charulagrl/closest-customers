from models import customer, office
from utils.maths_conversions import MathsConversions
import json

class DataLoader(object):
	'''Loads and reads raw data from file and convert it to data objects'''
	def __init__(self, data_store):
		self.path = None
		self.customers = None
		self.data_store = data_store

	def load_json_data(self):
		with open('data.json') as data_file:
			data = json.load(data_file)

			self.customers = data["customers"]
			self.offices = data["offices"]

		self.create_customer_data()
		self.create_office_data()

	def create_customer_data(self):
		for customer in self.customers:
			self.create_customer(customer)

	def create_customer(self, ob):
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		user_id = ob["user_id"]

		latitude = MathsConversions.get_radian(float(latitude))
		longitude = MathsConversions.get_radian(float(longitude))

		new_customer = customer.Customer(user_id, name, latitude, longitude)
		self.data_store.add_customer(new_customer)

	def create_office_data(self):
		for office in self.offices:
			self.create_office(office)

	def create_office(self, ob):
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		user_id = ob["office_id"]

		latitude = MathsConversions.get_radian(float(latitude))
		longitude = MathsConversions.get_radian(float(longitude))

		new_office = office.Office(user_id, name, latitude, longitude)
		self.data_store.add_office(new_office)
