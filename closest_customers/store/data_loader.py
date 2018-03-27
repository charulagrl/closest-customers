from models import customer, office
from utils.maths_conversions import MathsConversions
import json

class DataLoader(object):
	'''Loads and reads raw data from file and convert it to data objects'''
	def __init__(self, path):
		self.path = path
		self.data = None

		self.load_json_data()

	def load_json_data(self):
		with open(self.path) as data_file:
			self.data = json.load(data_file)

	def get_customer_objects(self):
		customers = {}
		for customer in self.data["customers"]:
			new_customer = self.create_customer(customer)
			if not customers.get(new_customer.id):
				customers[new_customer.id] = new_customer
			else:
				print("ERROR: customer id already exists")

		return customers

	def create_customer(self, ob):
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		user_id = ob["user_id"]

		latitude = MathsConversions.get_radian(float(latitude))
		longitude = MathsConversions.get_radian(float(longitude))

		new_customer = customer.Customer(user_id, name, latitude, longitude)
		return new_customer

	def get_office_objects(self):
		offices = {}
		for office in self.data["offices"]:
			new_office = self.create_office(office)
			if not offices.get(new_office.id):
				offices[new_office.id] = new_office
			else:
				print("ERROR: office id already exists")
		return offices

	def create_office(self, ob):
		latitude = ob["latitude"]
		longitude = ob["longitude"]
		name = ob["name"]
		user_id = ob["office_id"]

		latitude = MathsConversions.get_radian(float(latitude))
		longitude = MathsConversions.get_radian(float(longitude))

		new_office = office.Office(user_id, name, latitude, longitude)
		return new_office
