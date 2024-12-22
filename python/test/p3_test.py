import unittest
from python.p3 import solve, solve_efficient

class TestLargestPrimeFactor(unittest.TestCase):
  def test_solve_2(self):
    self.assertEqual(solve(2), 2)

  def test_solve_3(self):
    self.assertEqual(solve(3), 3)

  def test_solve_4(self):
    self.assertEqual(solve(4), 2)

  def test_solve_6(self):
    self.assertEqual(solve(6), 3)

  def test_solve_10(self):
    self.assertEqual(solve(10), 5)

  def test_solve_13195(self):
    self.assertEqual(solve(13195), 29)

  def test_solve_600851475143(self):
    self.assertEqual(solve(600851475143), 6857)
      
  def test_solve_efficient_2(self):
    self.assertEqual(solve_efficient(2), 2)

  def test_solve_efficient_3(self):
    self.assertEqual(solve_efficient(3), 3)

  def test_solve_efficient_4(self):
    self.assertEqual(solve_efficient(4), 2)

  def test_solve_efficient_6(self):
    self.assertEqual(solve_efficient(6), 3)

  def test_solve_efficient_10(self):
    self.assertEqual(solve_efficient(10), 5)

  def test_solve_efficient_13195(self):
    self.assertEqual(solve_efficient(13195), 29)

  def test_solve_efficient_600851475143(self):
    self.assertEqual(solve_efficient(600851475143), 6857)

if __name__ == '__main__':
  unittest.main()