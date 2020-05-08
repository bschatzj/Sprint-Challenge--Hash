class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination 

def reconstruct_trip(tickets, length):
	trip = {}
	route = []
	for ticket in tickets:
		print(ticket.destination)
		trip[ticket.source] = ticket.destination
	for index in range(len(tickets)):
		if index == 0:
			route.append(trip['NONE'])
		else:
			key = route[index - 1]
			route.append(trip[key])
	print(route)
	return route