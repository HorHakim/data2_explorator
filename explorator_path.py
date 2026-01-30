class ExploratorPath:
	def __init__(self, explorator_id, starting_edge):
		self.explorator_id = explorator_id
		self.path = [starting_edge]


	def add_step_to_adventure(self, next_edge):
		self.path.append(next_edge)


	def compute_adventure_distance(self):
		return sum(self.path)


	def __gt__(self, other_explorator_path):
		return self.compute_adventure_distance() > other_explorator_path.compute_adventure_distance()


	def __repr__(self): # meilleur que __str__ car plus large scope
		return f"{self.explorator_id} distance : {self.compute_adventure_distance():.2f} km chemin: {self.path}\n"