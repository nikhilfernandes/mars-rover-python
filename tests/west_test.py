import unittest
import sys
sys.path.append('../src')
from src.coordinate import Coordinate
from src.direction import *


class WestTest(unittest.TestCase):

	def test_move_decrements_the_x_coordinate(self):        
		expected = West().move(Coordinate(1,2))
		self.assertEqual(expected.xPos, 0)

	def test_move_does_not_increments_the_y_coordinate(self):        
		expected = West().move(Coordinate(1,2))
		self.assertEqual(expected.yPos, 2)

	def test_left_changes_direction_to_south(self):
 		expected = West().left()
 		self.assertEqual(expected, South())

	def test_right_changes_direction_to_north(self):
 		expected = West().right()
 		self.assertEqual(expected, North()) 		

    

if __name__ == '__main__':
    unittest.main()