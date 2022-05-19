import unittest
from second import solutin

class TestFirstTask(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(solutin([1, 3, 6, 4, 1, 2]), 5)
        self.assertEqual(solutin([1, 2, 3]), 4)
        self.assertEqual(solutin([-1, -3]), 1)


