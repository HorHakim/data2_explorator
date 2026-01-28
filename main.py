import pandas


def prepare_data(edges_df):

	starting_nodes =  edges_df[edges_df["type_aretes"] == "depart"]["noeud_amont"].tolist()
	dict_upstream_downstream = {row["noeud_amont"]: row["noeud_aval"] for _, row in edges_df.iterrows()}
	ending_nodes =  set(edges_df[edges_df["type_aretes"] == "arrivee"]["noeud_aval"])
	
	return starting_nodes, dict_upstream_downstream, ending_nodes


def build_explorators_paths(starting_nodes, dict_upstream_downstream, ending_nodes):
	explorators_paths = {}

	for index, starting_node in enumerate(starting_nodes):
		current_path = [starting_node]

		while current_path[-1] not in ending_nodes:
			current_node = current_path[-1]
			next_node = dict_upstream_downstream[current_node]

			current_path.append(next_node)

		explorators_paths[f"explorator_{index}"] = current_path

	return  explorators_paths



if __name__ == "__main__":
	edges_df = pandas.read_csv("./parcours_explorateurs.csv")
	
	starting_nodes, dict_upstream_downstream, ending_nodes = prepare_data(edges_df)


	explorators_paths = build_explorators_paths(starting_nodes, dict_upstream_downstream, ending_nodes)


	for explorator_id, explorator_path in explorators_paths.items():
		print(explorator_id)
		print(explorator_path)
		print("-"*20)