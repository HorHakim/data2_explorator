class Edge:
	def __init__(self, edge_id, upstream_node, downstream_node, edge_type, distance):
		self.edge_id = edge_id
		self.upstream_node = upstream_node
		self.downstream_node = downstream_node
		self.edge_type = edge_type
		self.distance = distance


	def __radd__(self, other_object):
		return self.distance + other_object


	def __repr__(self):
		return self.edge_id