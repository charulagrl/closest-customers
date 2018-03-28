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
		try:
			with open(self.path) as data_file:
				self.data = json.load(data_file)
		except Exception as e:
			logging.error("Json Data loading failed. Please check your json file.")
			exit()

	def get_customer_objects(self):
		customers = {}
		for customer in self.data["customers"]:
			new_customer = self.create_customer(customer)
			if not customers.get(new_customer.id):
				customers[new_customer.id] = new_customer
			else:
				logging.error("customer id already exists")

		return customers

	def create_location(self, latitude, longitude):
		new_location = location.Location(float(latitude), float(longitude))
		return new_location

	def create_customer(self, ob):
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		user_id = ob["user_id"]

		location = self.create_location(latitude, longitude)
		new_customer = customer.Customer(user_id, name, location)
		return new_customer

	def get_office_objects(self):
		offices = {}
		for office in self.data["offices"]:
			new_office = self.create_office(office)
			if not offices.get(new_office.id):
				offices[new_office.id] = new_office
			else:
				logging.error("ERROR: office id already exists")
		return offices

	def create_office(self, ob):
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		user_id = ob["office_id"]

		location = self.create_location(latitude, longitude)
		new_office = office.Office(user_id, name, location)
		return new_office
