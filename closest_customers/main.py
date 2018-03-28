from models import customer
from store import data_loader, data_store
from controller import distance
from views import results
import logging
import sys


if __name__ == "__main__":
	logging.basicConfig(filename='logger.log', level=logging.INFO)
	args = sys.argv[1:]
	#create data-store
	data_store = data_store.DataStore()
	office_id = int(args[0])

	if not data_store.get_office_by_id(office_id):
		logging.error("Office id not found")
		exit()

	# Calculate distances between office and all customers
	distance = distance.Distance()
	distance.calculate_distances(data_store, office_id)

	# display customer details sorted by user id
	results.Result.display_sorted_by_id_result(distance.distances, data_store.customers)
