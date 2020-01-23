import unittest
import sys
sys.path.append('../src')
from src.coordinate import Coordinate
from src.direction import *

class SouthTest(unittest.TestCase):

	def test_move_decrements_the_y_coordinate(self):        
		expected = South().move(Coordinate(1,2))
		self.assertEqual(expected.yPos, 1)

	def test_move_does_not_increments_the_x_coordinate(self):        
		expected = South().move(Coordinate(1,2))
		self.assertEqual(expected.xPos, 1)

	def test_left_changes_direction_to_east(self):
 		expected = South().left()
 		self.assertEqual(expected, East())

	def test_right_changes_direction_to_west(self):
 		expected = South().right()
 		self.assertEqual(expected, West()) 		

    

if __name__ == '__main__':
    unittest.main()