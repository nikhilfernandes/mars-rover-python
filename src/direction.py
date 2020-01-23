from src.coordinate import Coordinate

class Direction:

	def move(self, coordinate):
		raise NotImplementedError("Method not implemented") 

	def left(self):
		raise NotImplementedError("Method not implemented") 	

	def right(self):
		raise NotImplementedError("Method not implemented") 			

class North(Direction):

	def __init__(self):
		self.key = "North"        

	def __eq__(self, other): 
		if not isinstance(other, North):            
			return NotImplemented

		return self.key == other.key

	def move(self, coordinate):
		return Coordinate(coordinate.xPos, coordinate.yPos+1)

	def left(self):
		return West() 	

	def right(self):
		return East()

class South(Direction):
	def __init__(self):
		self.key = "South"        

	def __eq__(self, other): 
		if not isinstance(other, South):            
			return NotImplemented

		return self.key == other.key	

	def move(self, coordinate):
		return Coordinate(coordinate.xPos, coordinate.yPos-1)

	def left(self):
		return East() 	

	def right(self):
		return West()

class East(Direction):

	def __init__(self):
		self.key = "East"        

	def __eq__(self, other): 
		if not isinstance(other, East):            
			return NotImplemented

		return self.key == other.key	

	def move(self, coordinate):
		return Coordinate(coordinate.xPos+1, coordinate.yPos)

	def left(self):
		return North() 	

	def right(self):
		return South()

class West(Direction):

	def __init__(self):
		self.key = "West"        

	def __eq__(self, other): 
		if not isinstance(other, West):            
			return NotImplemented

		return self.key == other.key

	def move(self, coordinate):
		return Coordinate(coordinate.xPos-1, coordinate.yPos)

	def left(self):
		return South() 	

	def right(self):
		return North()								