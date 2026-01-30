from explorator_path import ExploratorPath
from edge import Edge


import pandas



def prepare_data(edges_df):

	starting_nodes =  edges_df[edges_df["type_aretes"] == "depart"]["noeud_amont"].tolist()
	
	dict_edges = {}
	for _, row in edges_df.iterrows():
		edge_id = row["arete_id"]
		upstream_node = row["noeud_amont"]
		downstream_node = row["noeud_aval"]
		edge_type = row["type_aretes"]
		distance = row["distance"]

		dict_edges[upstream_node] = Edge(edge_id, upstream_node, downstream_node, edge_type, distance)
	
	return starting_nodes, dict_edges





def build_explorators_paths(starting_nodes, dict_edges):
	dict_explorators_paths = {}
	list_explorators_paths = []


	for index, starting_node in enumerate(starting_nodes):
		explorator_id = f"explorator_{index}"
		starting_edge = dict_edges[starting_node]

		current_explorator_path = ExploratorPath(explorator_id, starting_edge)

		while current_explorator_path.path[-1].edge_type != "arrivee":
			next_node = current_explorator_path.path[-1].downstream_node
			next_edge = dict_edges[next_node]
			
			current_explorator_path.add_step_to_adventure(next_edge)


	
		dict_explorators_paths[explorator_id] = current_explorator_path
		list_explorators_paths.append(current_explorator_path)


	return dict_explorators_paths, list_explorators_paths




if __name__ == "__main__":
	edges_df = pandas.read_csv("./parcours_explorateurs.csv")

	starting_nodes, dict_edges = prepare_data(edges_df)

	dict_explorators_paths, list_explorators_paths = build_explorators_paths(starting_nodes, dict_edges)


	list_explorators_paths.sort(reverse=True)

	print(list_explorators_paths)