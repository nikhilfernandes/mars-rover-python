class Coordinate:
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos

	def __eq__(self, other): 
		if not isinstance(other, Coordinate):            
			return NotImplemented

		return self.xPos == other.xPos and self.yPos == other.yPos
