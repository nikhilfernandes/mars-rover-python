import unittest
import sys
sys.path.append('../src')
from src.coordinate import Coordinate
from src.rover import Rover
from src.plateau import Plateau
from src.direction import *
from src.instruction_exception import InstructionException

class RoverTest(unittest.TestCase):

	def setUp(self):
		self.coordinate = Coordinate(1,2)
		self.plateau = Plateau(5,5)

	def test_move_when_pointed_north_in_y_direction_upwards(self):
		rover = Rover(self.coordinate, North())
		rover.move(self.plateau.is_coordinate_with_bounds)
		self.assertEqual(rover.coordinate, Coordinate(1,3))		

	def test_move_when_pointed_south_in_y_direction_downwards(self):
		rover = Rover(self.coordinate, South())
		rover.move(self.plateau.is_coordinate_with_bounds)
		self.assertEqual(rover.coordinate, Coordinate(1,1))				

	def test_move_when_pointed_west_in_x_direction_backwards(self):		
		rover = Rover(self.coordinate, West())		
		rover.move(self.plateau.is_coordinate_with_bounds)
		self.assertEqual(rover.coordinate, Coordinate(0,2))						

	def test_move_when_pointed_east_in_x_direction_forward(self):		
		rover = Rover(self.coordinate, East())		
		rover.move(self.plateau.is_coordinate_with_bounds)
		self.assertEqual(rover.coordinate, Coordinate(2,2))								

	def test_turn_changes_direction_for_L_instruction(self):		
		rover = Rover(self.coordinate, East())
		rover.turn("L")
		self.assertEqual(rover.direction, North())										

	def test_turn_changes_direction_for_R_instruction(self):		
		rover = Rover(self.coordinate, East())
		rover.turn("R")
		self.assertEqual(rover.direction, South())												

	def test_turn_raised_exception_for_incorrect_instruction(self):		
		rover = Rover(self.coordinate, East())		
		self.assertRaises(InstructionException, rover.turn("W"))

    

if __name__ == '__main__':
    unittest.main()