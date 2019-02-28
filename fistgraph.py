class Node(object):
	def __init__(self,value):
		self.value = value
		self.edges = []
##END

class Edge(object):
	def  __init__(self, value, node_from, node_to):
		self.value = value
		self.nome_from = node_from
		self.node_to = node_to
##end

class Graph(object):
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges
	
	def insert_node(self, new_node_val):
		new_node = Node(new_node_val)
		self.nodes.append(new_node)

	def insert_edge(self, new_edge_val, node_from_val, node_to_val):
		from_found = None 
		to_found = None 
		
		for node in self.nodes:
			if node_from_val == node.value:
				from_found = node
			if node_to_val == node.value:
				to_found = node

		if from_found == None:
			from_found = Node(node_from_val)
			self.nodes.append(from_found)

		if to_found == None:
			to_found = Node(node_to_val)
			self.nodes.append(to_found)

		new_edge = Edge(new_edge_val, from_found, to_found)
		from_found.edges.append(new_edge)
		to_found.edges.append(new_edge)
		self.edges.append(new_edge)