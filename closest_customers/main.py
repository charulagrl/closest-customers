from models import customer
from store import data_loader, data_store
from controller import distance
from views import results
import sys


if __name__ == "__main__":
	#create data-store
	data_store = data_store.DataStore()
	#load data into data-store
	data_loader = data_loader.DataLoader(data_store)
	data_loader.load_json_data()

	# get the value of minimum distance limit from command line
	args = sys.argv[1:]
	distance_limit = int(args[0])
	office_id = int(args[1])

	if not data_store.offices.get(office_id, None):
		print ("Office id not found")
		exit()

	# Calculate distances between office and all customers
	distance = distance.Distance(distance_limit)
	distance.calculate_distances(data_store, office_id)

	# display customer details sorted by user id
	results.Result.display_sorted_by_id_result(distance.distances, data_store.customers)


