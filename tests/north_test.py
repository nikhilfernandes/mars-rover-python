import unittest
import sys
sys.path.append('../src')
from src.coordinate import Coordinate
from src.direction import *

class NorthTest(unittest.TestCase):

	def test_move_increments_the_y_coordinate(self):        
		expected = North().move(Coordinate(1,2))
		self.assertEqual(expected.yPos, 3)

	def test_move_does_not_increments_the_x_coordinate(self):        
		expected = North().move(Coordinate(1,2))
		self.assertEqual(expected.xPos, 1)

	def test_left_changes_direction_to_west(self):
 		expected = North().left()
 		self.assertEqual(expected, West())

	def test_right_changes_direction_to_east(self):
 		expected = North().right()
 		self.assertEqual(expected, East()) 		

    

if __name__ == '__main__':
    unittest.main()