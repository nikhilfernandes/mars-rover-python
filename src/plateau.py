class Plateau:
	def __init__(self, xMax, yMax):
		self.xMax = xMax
		self.yMax = yMax

	def is_coordinate_with_bounds(self, coordinate):
		return self.xMax >= coordinate.xPos and self.yMax >= coordinate.yPos and coordinate.xPos >= 0 and coordinate.yPos >= 0