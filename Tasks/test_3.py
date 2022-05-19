import unittest
from task_3 import solution

class TestFirstTask(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(solution([1,5,2,1,4,0]), 11)
        self.assertEqual(solution([1, 1]), 1)
        self.assertEqual(solution([2, 1,1,2]), 6)
        self.assertEqual(solution([1, 0, 1, 2]), 6)
        self.assertEqual(solution([0, 0, 1, 0]), 2)
        self.assertEqual(solution([0, 0, 0, 0]), 0)


