class Result(object):
	
	@classmethod
	def display_sorted_by_id_result(self, distances, customers):
		for key in sorted(distances.keys()):
			customer = customers.get(key, None)

			print ("Customer details: user_id: " + str(customer.id) + " name: " + customer.name)
