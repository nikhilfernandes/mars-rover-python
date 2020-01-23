import unittest
import sys
sys.path.append('../src')
from src.coordinate import Coordinate
from src.direction import *


class EastTest(unittest.TestCase):

	def test_move_increments_the_x_coordinate(self):        
		expected = East().move(Coordinate(1,2))
		self.assertEqual(expected.xPos, 2)

	def test_move_does_not_increments_the_y_coordinate(self):        
		expected = East().move(Coordinate(1,2))
		self.assertEqual(expected.yPos, 2)

	def test_left_changes_direction_to_north(self):
 		expected = East().left()
 		self.assertEqual(expected, North())

	def test_right_changes_direction_to_south(self):
 		expected = East().right()
 		self.assertEqual(expected, South()) 		

    

if __name__ == '__main__':
    unittest.main()