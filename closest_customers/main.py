from models import customer
from models import location
from store import data_loader, data_store
from controller import distance


if __name__ == "__main__":
	data_store = data_store.DataStore()
	data_loader = data_loader.DataLoader(data_store)
	data_loader.load_json_data()
