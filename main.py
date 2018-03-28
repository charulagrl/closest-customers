import logging
import sys
import argparse
from closest_customers.models import customer
from closest_customers.store import data_loader, data_store
from closest_customers.controller import distance
from closest_customers.views import results
from closest_customers.config import Production



if __name__ == "__main__":

	logging.basicConfig(filename='logger.log', level=logging.INFO)

	parser = argparse.ArgumentParser()
	parser.add_argument("id", type=int, help="Office ID from which to calculate the distance")
	args = parser.parse_args()	

	# create data-store        # does this comment is required, it is obvious from the code
	data_store = data_store.DataStore(Production.data_file_path)
	office_id = int(args.id)

	if not data_store.get_office_by_id(office_id):
		logging.error("Office id not found, please pass a valid office id")
		exit()

	# Calculate distances between office and all customers    # is this commend needed, ditto
	distance = distance.Distance()
	distance.calculate_distances(data_store, office_id)

	# display customer details sorted by user id
	results.Result.display_sorted_by_id_result(distance.distances, data_store.customers)
