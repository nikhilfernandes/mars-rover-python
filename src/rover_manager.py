class RoverManager:

	def __init__(self, plateau, rover):
		self.plateau = plateau
		self.rover = rover


	def perform(self, instructions):
		for instruction in instructions: 
			if instruction == "M":
				self.rover.move(self.plateau.is_coordinate_with_bounds)
			else:
				self.rover.turn(instruction)
    		
