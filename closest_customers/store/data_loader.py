from models import customer, office, location
from config import Config
import logging
import json

class DataLoader(object):
	'''Loads and reads raw data from file and convert it to data objects'''
	def __init__(self):
		self.path = Config.path
		self.data = None

		self.load_json_data()

	def load_json_data(self):
		'''Load json data from file'''
		try:
			with open(self.path) as data_file:
				self.data = json.load(data_file)
		except Exception as e:
			logging.error("Json Data loading failed. Please check your json file.")
			exit()

	def create_location(self, latitude, longitude):
		'''Create a location object'''
		try:
			latitude = float(latitude)
			longitude = float(longitude)
			if latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180:
				new_location = location.Location(latitude, longitude)
				return new_location
		except Exception as e:
			logging.error("Invalid values of latitude and longitude")

	def get_customer_objects(self):
		'''Create a dict of customer object'''
		customers = {}
		if not self.data.get("customers", None):
			logging.error("Customers list not present in data")
			exit()

		for customer in self.data["customers"]:
			user_id = customer.get('user_id', None)

			if user_id and not customers.get(user_id, None):
				new_customer = self.create_customer(customer)
				if new_customer:
					customers[new_customer.id] = new_customer
			else:
				logging.error("customer id already exists")

		return customers

	def create_customer(self, ob):
		'''Create a customer object'''
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		user_id = ob["user_id"]

		location = self.create_location(latitude, longitude)
		if location:
			if self.is_valid(user_id, name):
				new_customer = customer.Customer(user_id, name, location)
				return new_customer
			else:
				logging.error("User id {} or name {} is invalid".format(user_id, name))

	def get_office_objects(self):
		'''Create dict of office objects'''
		offices = {}

		if not self.data.get("offices", None):
			logging.error("Offices list not present in data")
			exit()

		for office in self.data["offices"]:
			office_id = office.get("office_id", None)

			if office_id and not offices.get(office_id, None):
				new_office = self.create_office(office)

				if new_office:
					offices[new_office.id] = new_office
			else:
				logging.error("Office id {} already exists".format(office_id))

		return offices

	def create_office(self, ob):
		'''Create a single office object'''
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		office_id = ob["office_id"]

		location = self.create_location(latitude, longitude)
		if location:
			if self.is_valid(office_id, name):
				new_office = office.Office(office_id, name, location)
				return new_office
			else:
				logging.error("Office id {} or name {} is invalid".format(office_id, name))

	def is_valid(self, id, name):
		'''Check if id and name is valid'''
		if isinstance(id, int) and isinstance(name, basestring) and name != "":
			return True
		else:
			return False
