from src.instruction_exception import InstructionException
from src.out_of_plateau_exception import OutOfPlateauException
class Rover():

	def __init__(self, coordinate, direction):
		self.coordinate = coordinate
		self.direction = direction

	def move(self, bound_func):
		coordinate = self.direction.move(self.coordinate)
		if bound_func(coordinate):
			self.coordinate = coordinate
		else:			
			raise OutOfPlateauException()
				

	def turn(self, instruction):	
		if instruction == "L":
			self.direction = self.direction.left()
		elif instruction == "R":
			self.direction = self.direction.right()
		else:
			raise InstructionException()
		
