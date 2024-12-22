import unittest
from python.p1 import solve, solve2

class TestSumOfMultiples(unittest.TestCase):
  def test_solve_10(self):
    self.assertEqual(solve(10), 23)

  def test_solve_1000(self):
    self.assertEqual(solve(1000), 233168)

  def test_solve2_10(self):
    self.assertEqual(solve2(10), 23)

  def test_solve2_1000(self):
    self.assertEqual(solve2(1000), 233168)

if __name__ == '__main__':
  unittest.main()