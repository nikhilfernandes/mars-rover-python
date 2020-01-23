import unittest
import sys
sys.path.append('../src')
from src.coordinate import Coordinate

class CoordinateTest(unittest.TestCase):

    def test_coordinate_Created(self):
        coordinate = Coordinate(1,2)
        self.assertEqual(coordinate, Coordinate(1,2))
        

    

if __name__ == '__main__':
    unittest.main()