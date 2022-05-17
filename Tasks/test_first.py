import unittest
from first import solution

class TestFirstTask(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(solution(1041), 5)
        self.assertEqual(solution(32), 0)
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(15), 0)

    def test_values(self):
        self.assertRaises(ValueError, solution, -2)
        self.assertRaises(ValueError, solution, 5.5)
        self.assertRaises(ValueError, solution, -22.4)
