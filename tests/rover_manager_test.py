import unittest
import sys
sys.path.append('../src')
from src.coordinate import Coordinate
from src.rover import Rover
from src.plateau import Plateau
from src.rover_manager import RoverManager
from src.direction import *

class RoverManagerTest(unittest.TestCase):

	def test_first_input(self):
		coordinate = Coordinate(1,2)	
		plateau = Plateau(5,5)
		rover = Rover(coordinate, North())
		RoverManager(plateau, rover).perform("LMLMLMLMM")		
		self.assertEqual(rover.coordinate, Coordinate(1,3))
		self.assertEqual(rover.direction, North())		

	def test_second_input(self):
		coordinate = Coordinate(3,3)	
		plateau = Plateau(5,5)
		rover = Rover(coordinate, East())
		RoverManager(plateau, rover).perform("MMRMMRMRRM")		
		self.assertEqual(rover.coordinate, Coordinate(5,1))
		self.assertEqual(rover.direction, East())				
